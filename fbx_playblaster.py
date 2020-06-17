from maya import cmds, mel
# import maya.standalone
import os
import pprint
import math
import sys


def build_camera(bb=None, cam_height=None, res_w=1920, res_h=1080):
    # Get the set/scene size from the bounding box
    scene_bb = bb
    # Find the center from the bounding box
    x_center = scene_bb[3] - ((scene_bb[3] - scene_bb[0]) / 2)
    y_center = scene_bb[4] - ((scene_bb[4] - scene_bb[1]) / 2)
    z_center = scene_bb[5] - ((scene_bb[5] - scene_bb[2]) / 2)
    bb_center = [x_center, y_center, z_center]
    cmds.xform(piv=[x_center, y_center, z_center])

    user_cam_height = cam_height
    if user_cam_height:
        cam_height = float(user_cam_height) + scene_bb[1]
    else:
        cam_height = scene_bb[4] - scene_bb[1]
    # Create a new camera and fit it to the current view
    cam = cmds.camera(n='pb_follow_cam')
    active_panel = cmds.getPanel(wf=True)
    cmds.lookThru(cam)
    cmds.viewFit()
    cmds.modelEditor(active_panel, e=True, displayTextures=True)
    cmds.modelEditor(active_panel, e=True, udm=False)
    
    # Get the position of the new camera after placement
    cam_pos = cmds.xform(q=True, ws=True, t=True)
    # Separate out the mins and maxs of the bounding box for triangulation
    x_min = scene_bb[0]
    x_max = scene_bb[3]
    y_min = scene_bb[1]
    y_max = scene_bb[4]
    z_min = scene_bb[2]
    z_max = scene_bb[5]
    # Get the cube root hypotenuse of the bounding box to calculate the overall scene's widest distance
    cube_diff = math.pow((x_max - x_min), 3) + math.pow((y_max - y_min), 3) + math.pow((z_max - z_min), 3)
    max_hypotenuse = cube_diff ** (1. / 3.)
    # Cut the width in half to create a 90 degree angle
    res_width = float(res_w)
    res_height = float(res_h)
    aspect_ratio = res_width / res_height
    height = (y_max - y_min)
    width = (x_max - x_min)
    depth = (z_max - z_min)

    half_width = max_hypotenuse / 2
    # Get the horizontal aperture. Only the inch aperture is accessible, so mm aperture and field of view
    # must be calculated from that
    horizontalApertureInch = cmds.getAttr('%s.horizontalFilmAperture' % cam[1])
    # convert to mm
    horizontalAperture_mm = 2.54 * horizontalApertureInch * 10
    # Get focal length
    focalLength = cmds.getAttr('%s.focalLength' % cam[1])
    # Calculate FOV from horizontal aperture and focal length
    fov = math.degrees(2 * math.atan(horizontalAperture_mm / (focalLength * 2)))
    # Cut the FOV in half to get angle of right angle.
    half_angle = fov / 2
    # Calculate the distance for the camera
    angle_tan = math.tan(half_angle)
    distance = cam_pos[2] - (half_width / angle_tan)
    # Set the new camera distance and height
    cmds.setAttr('%s.ty' % cam[0], cam_height)
    cmds.setAttr('%s.tz' % cam[0], distance)
    # Get the new camera position
    new_cam_pos = cmds.xform(q=True, t=True, ws=True)

    cam_height = (new_cam_pos[1] - bb_center[1])

    cam_dist = new_cam_pos[2] - bb_center[2]
    cam_angle = -1 * (math.degrees(math.atan(cam_height / cam_dist)))
    # Set the declination angle
    cmds.setAttr('%s.rx' % cam[0], cam_angle)
    # Group the camera, center the pivot, and animate the rotation

    grp = cmds.group(n='_playblast_cam')
    cmds.xform(piv=bb_center)
    cameras = cmds.listCameras(p=True, o=True)
    for camera in cameras:
        if camera == cam[0]:
            cmds.setAttr('%s.renderable' % camera, 1)
            cmds.setAttr('%s.translate' % camera, lock=True)
            cmds.setAttr('%s.rotate' % camera, lock=True)
            cmds.setAttr('%s.scale' % camera, lock=True)
        else:
            cmds.setAttr('%s.renderable' % camera, 0)
    return [cam, bb_center, scene_bb, max_hypotenuse, grp]


def build_maya_scene(_path=None, _fbx=None, root=None):
    """
    This method builds out the Maya scene from an FBX file
    :param _path: The folder path to the FBX file
    :param _fbx: The name of the FBX file
    :param root: The root joint of the character
    :return: 
    """
    new_file = cmds.file(new=True, f=True)
    fbx_filepath = _path
    fbx_filename = _fbx
    fbx_file = os.path.join(fbx_filepath, fbx_filename)
    fbx = cmds.file(fbx_file, i=True, applyTo=':')
    cmds.select(root, r=True)
    selected = cmds.ls(sl=True)
    if selected:
        print('Shit:', selected)
        bb = cmds.xform(bb=True, q=True)
        print('Bounding Box: %s' % bb)
    else:
        print('DAMN!!!!', selected)
        bb = [-1.0, 0.0, -1.0, 1.0, 1.0, 1.0]
    bb_x = abs(bb[0]) + abs(bb[3])
    bb_y = abs(bb[1]) + abs(bb[4])
    bb_z = abs(bb[2]) + abs(bb[5])

    cam_data = build_camera(bb=bb)
    print('Cam Data: %s' % cam_data)
    camera_grp = cam_data[4]
    cmds.pointConstraint(selected[0], camera_grp, mo=True, skip='y', w=1)

    shader = cmds.shadingNode('blinn', asShader=True, n='_ground_checker_mat')
    checker = cmds.shadingNode('checker', asTexture=True, n='_checkerboard')
    placement = cmds.shadingNode('place2dTexture', asUtility=True, n='_checker_placement')
    cmds.setAttr('%s.repeatU' % placement, bb_y)
    cmds.setAttr('%s.repeatV' % placement, bb_y)
    cmds.connectAttr('%s.outUvFilterSize' % placement, '%s.uvFilterSize' % checker)
    cmds.connectAttr('%s.outUV' % placement, '%s.uvCoord' % checker)
    cmds.connectAttr('%s.outColor' % checker, '%s.color' % shader)
    cmds.setAttr('%s.transparency' % shader, 0.85, 0.85, 0.85)
    plane = cmds.polyPlane(n='_ground_plane', cuv=1, h=10000, w=10000, sh=100, sw=100)
    cmds.hyperShade(a=shader)
    
    # Get min and max frames
    cmds.select(selected[0], r=True)
    cmds.select(hi=True)
    mel.eval('setPlaybackRangeToMinMax;')
    
    mel.eval('setSceneTimecodeVisibility(true);')
    mel.eval('setCurrentFrameVisibility(true);')

    # Save the file
    base_name = os.path.splitext(fbx_filename)[0]
    scene_name = '%s_fbx_playblast' % base_name
    scene_name = os.path.join(_path, scene_name)
    cmds.file(rename=scene_name)
    cmds.file(save=True, type='mayaAscii')

    # Create a playblast
    # TODO: Check for MOV install and possibly load the plugin

    save_data = cmds.playblast(format='qt', filename=scene_name, sqt=0, cc=True, v=True, os=True, fp=4, p=100, qlt=80,
                               h=1080, w=1920)
    print(save_data)


def fbx_to_playblast():
    if len(sys.argv) > 1:
        full_path = sys.argv[1]
        joint_name = sys.argv[2]
        root_path = os.path.dirname(full_path)
        file_name = os.path.basename(full_path)
        build_maya_scene(_path=root_path, _fbx=file_name, root=joint_name)
    else:
        return False

def batch_process_fbx_playblasts(_path=None, _root=None):
    if _path and _root:
        if os.path.exists(_path):
            collect = os.walk(_path)
            for roots, dirs, files in collect:
                if files:
                    for f in files:
                        if f.endswith('.fbx'):
                            print('Building Playblast...', f)
                            build_maya_scene(_path=roots, _fbx=f, root=_root)


if __name__ == '__main__':
    start_path = 'C:/Users/sleep/OneDrive/Documents/Scripts/Python/Utilities/FBX_Editor/'
    root = 'Reference'
    batch_process_fbx_playblasts(_path=start_path, _root=root)
    
#     # build_maya_scene(_path='C:/Users/sleep/OneDrive/Documents/Scripts/Python/Utilities/FBX_Editor/raw_data/Run_Adam_001_006_Adam_Sneakers.fbx', root='Reference')
#     fbx_to_playblast()

# Command Line setup
# command = 'python("C:/Users/sleep/OneDrive/Documents/Scripts/Python/Utilities/FBX_Editor/fbx_playblaster.py")'

