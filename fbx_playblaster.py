import maya.standalone
maya.standalone.initialize(name='python')
from maya import cmds
import os
import math
import sys
import json
import ast
from PySide2 import QtCore, QtWidgets
from ui import ui_devilsRoto_pb_queue as popup


class maya_playblaster:
    def __init__(self):
        self.data = None

    def solo_renderable(self, solo_cam):
        # Disable all cameras as renderable
        # and store the original states
        cams = cmds.ls(type='camera')
        print('cams: %s' % cams)
        states = {}
        for cam in cams:
            states[cam] = cmds.getAttr(cam + '.rnd')
            cmds.setAttr(cam + '.rnd', 0)

        # Change the solo cam to renderable
        cmds.setAttr(solo_cam + '.rnd', 1)

        try:
            yield
        finally:
            # Revert to original state
            for cam, state in states.items():
                cmds.setAttr(cam + '.rnd', state)

    def build_geo_bones(self):
        # Create geo bones from joints
        print('Building geo boxes...')

        joints = cmds.ls(type='joint')

        joint_data = {}
        bones = []
        for joint in joints:
            children = cmds.listRelatives(joint, c=True)
            if children and len(children) >= 1:
                joint_data[joint] = {
                    'children': children
                }

        # This will need a way to determine varying joint hierarchies!  Spine to arms to legs, et cetera.
        for joint, data in joint_data.items():
            j_children = data['children']
            j_radius = cmds.getAttr('%s.radius' % joint)
            for child in j_children:
                j_pos = cmds.xform(joint, q=True, t=True, ws=True)
                c_pos = cmds.xform(child, q=True, t=True, ws=True)
                half_rad = j_radius / 2

                # Find the distance to the next joint
                distance = math.sqrt(
                    ((c_pos[0] - j_pos[0]) ** 2) + ((c_pos[1] - j_pos[1]) ** 2) + ((c_pos[2] - j_pos[2]) ** 2))
                height = distance

                # Build cubes
                new_cube = cmds.polyCube(h=half_rad, d=half_rad, w=height, n='%s_bone' % joint)
                bones.append(new_cube)
                new_piv_dist = 0.0 - (height / 2.0)
                cmds.xform(new_cube, piv=(new_piv_dist, 0.0, 0.0))

                # Properly align and attach cubes to bones
                point = cmds.pointConstraint(joint, new_cube, mo=False)
                aim = cmds.aimConstraint(child, new_cube)
                cmds.delete(point)
                cmds.delete(aim)
                cmds.parentConstraint(joint, new_cube, mo=True)
        cmds.select(clear=True)
        for bone in bones:
            cmds.select(bone[0], add=True)
        group = cmds.group(n='_fbx_geo_bones')
        return group

    def build_camera(self, bb=None, cam_height=None, res_w=1920, res_h=1080):
        # Get the set/scene size from the bounding box
        scene_bb = bb
        # Find the center from the bounding box
        x_center = scene_bb[3] - ((scene_bb[3] - scene_bb[0]) / 2)
        y_center = scene_bb[4] - ((scene_bb[4] - scene_bb[1]) / 2)
        z_center = scene_bb[5] - ((scene_bb[5] - scene_bb[2]) / 2)
        bb_center = [x_center, y_center, z_center]
        print('BB Center: %s' % bb_center)
        cmds.xform(piv=[x_center, y_center, z_center])

        user_cam_height = cam_height
        if user_cam_height:
            cam_height = float(user_cam_height) + scene_bb[1]
        else:
            cam_height = scene_bb[4] - scene_bb[1]
        # Create a new camera and fit it to the current view
        cam = cmds.camera(n='pb_follow_cam')
        # Set the renderable camera
        self.solo_renderable(cam[0])
        active_panel = cmds.getPanel(wf=True)
        print('active_panel: %s' % active_panel)
        # cmds.lookThru(cam)
        # cmds.viewFit()
        cmds.modelEditor(active_panel, e=True, displayTextures=True)
        cmds.modelEditor(active_panel, e=True, udm=False)

        # Get the position of the new camera after placement
        cam_pos = cmds.xform(q=True, ws=True, t=True)
        print('cam_pos original: %s' % cam_pos)
        # Separate out the mins and maxs of the bounding box for triangulation
        x_min = scene_bb[0]
        x_max = scene_bb[3]
        y_min = scene_bb[1]
        y_max = scene_bb[4]
        z_min = scene_bb[2]
        z_max = scene_bb[5]
        # Get the cube root hypotenuse of the bounding box to calculate the overall scene's widest distance
        cube_diff = math.pow((x_max - x_min), 3) + math.pow((y_max - y_min), 3) + math.pow((z_max - z_min), 3)
        print('cubic_diff: %s' % cube_diff)
        max_hypotenuse = cube_diff ** (1. / 3.)
        print('max_hypotenuse: %s' % max_hypotenuse)
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
        print('horz aperature: %s' % horizontalApertureInch)
        # convert to mm
        horizontalAperture_mm = 2.54 * horizontalApertureInch * 10
        print('horz app mm: %s' % horizontalAperture_mm)
        # Get focal length
        focalLength = cmds.getAttr('%s.focalLength' % cam[1])
        print('focal length: %s' % focalLength)
        # Calculate FOV from horizontal aperture and focal length
        fov = math.degrees(2 * math.atan(horizontalAperture_mm / (focalLength * 2)))
        print('fov: %s' % fov)
        # Cut the FOV in half to get angle of right angle.
        half_angle = fov / 2
        # Calculate the distance for the camera
        angle_tan = math.tan(half_angle)
        print('Camera Distance math ---------------------------------------------')
        print('cam_pos[2]: %s' % cam_pos[2])
        print('half_width: %s' % half_width)
        print('angle_tan: %s' % angle_tan)
        distance = cam_pos[2] - (half_width / angle_tan)
        print('deistance - cam_pos[2] - (half_width / angle_tan) = %s' % distance)
        # Set the new camera distance and height
        cmds.setAttr('%s.ty' % cam[0], cam_height)
        cmds.setAttr('%s.tz' % cam[0], distance)
        # Get the new camera position
        new_cam_pos = cmds.xform(q=True, t=True, ws=True)
        print('new_cam_pos: %s' % new_cam_pos)

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

    def build_maya_scene(self,_path=None, _fbx=None, root=None):
        """
        This method builds out the Maya scene from an FBX file.  It creates an empty Maya scene, imports the FBX into
        the new scene and creates a camera that follows the mocap data.  A checkered floor with some transparency is
        also created to help understand the movement and contact points for the feet.
        :param _path: The folder path to the FBX file
        :param _fbx: The name of the FBX file
        :param root: The root joint of the character
        :return:
        """
        # Create a clean Maya file
        cmds.file(new=True, f=True)

        # Take in the folder path, the fbx filename and the root joint name (usually "Reference" or "Hips" for mocap.
        fbx_filepath = _path
        fbx_filename = _fbx
        fbx_file = os.path.join(fbx_filepath, fbx_filename)

        # Import the FBX into the Maya scene
        fbx = cmds.file(fbx_file, i=True, applyTo=':')

        # Select the skeleton root
        try:
            cmds.select(root, r=True)
        except ValueError as e:
            # The root selection can't be found.
            print('Shit hit the fan.  Can\'t find %s in the scene: %s' % (root, e))
            return False
        selected = cmds.ls(sl=True)
        if selected:
            # build GEO Bones
            bones = self.build_geo_bones()
            cmds.select(bones, add=True)
            # The FBX skeleton is found and selected!
            # Get the Bounding Box information
            bb = cmds.xform(bb=True, q=True)
            print('Bounding Box: %s' % bb)
            cmds.select(selected, r=True)
        else:
            print('Object not selected, set a default.  This should never work.', selected)
            bb = [-1.0, 0.0, -1.0, 1.0, 1.0, 1.0]

        # Set Bounding Box Absolute length
        bb_x = abs(bb[0]) + abs(bb[3])
        bb_y = abs(bb[1]) + abs(bb[4])
        bb_z = abs(bb[2]) + abs(bb[5])

        # Run the build_camera routine on the bounding boxes.
        cam_data = self.build_camera(bb=bb)
        print('Cam Data: %s' % cam_data)

        # Get the group camera data
        camera_grp = cam_data[4]

        # Point constrain the camera to both the X and Z axis so that Y axis translations are not taken into account.
        cmds.pointConstraint(selected[0], camera_grp, mo=True, skip='y', w=1)

        # Build a check
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
        geo = cmds.ls(type='mesh')
        shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='_ground_checker_mat_SG')
        cmds.connectAttr((shader + '.outColor'), (shading_group + '.surfaceShader'), f=True)
        cmds.sets(geo, e=True, forceElement=shading_group)

        # Get min and max frames
        cmds.select(selected[0], r=True)
        cmds.select(hi=True)

        # mel.eval('setPlaybackRangeToMinMax;')
        _time = cmds.keyframe(q=True, time=(-999999999, 999999999))
        sorted_time = sorted(_time)
        min_time = sorted_time[0]
        max_time = sorted_time[-1]

        cmds.playbackOptions(ast=min_time, aet=max_time, min=min_time, max=max_time)

        # mel.eval('setSceneTimecodeVisibility(true);')
        # mel.eval('setCurrentFrameVisibility(true);')

        # Save the file
        base_name = os.path.splitext(fbx_filename)[0]
        scene_name = '%s_fbx_playblast' % base_name
        print('scene_name: %s' % scene_name)
        scene_name = os.path.join(_path, scene_name)
        save_name = '%s.ma' % scene_name
        cmds.file(rename=save_name)
        cmds.file(save=True, type='mayaAscii')

        # Create a playblast
        # TODO: Check for MOV install and possibly load the plugin

        save_data = cmds.playblast(format='qt', filename=scene_name, sqt=0, cc=True, v=True, os=True, fp=4, p=100,
                                   qlt=80, h=1080, w=1920, fo=True)
        print(save_data)

    def fbx_to_playblast(self):
        if len(sys.argv) > 1:
            full_path = sys.argv[1]
            joint_name = sys.argv[2]
            root_path = os.path.dirname(full_path)
            file_name = os.path.basename(full_path)
            self.build_maya_scene(_path=root_path, _fbx=file_name, root=joint_name)
        else:
            return False

    def batch_process_fbx_playblasts(self, _path=None, _root=None):
        if _path and _root:
            if os.path.exists(_path):
                print('PATH EXISTS: %s' % _path)
                if _path.endswith('.fbx'):
                    print('Building Playblast...', _path)
                    self.build_maya_scene(_path=os.path.dirname(_path), _fbx=os.path.basename(_path), root=_root)

    # def playblast_queue(self, QtWidgets


class queue_popup(QtWidgets.QWidget):
    def __init__(self, parent=None, data=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = popup.Ui_Form()
        self.ui.setupUi(self)
        self.data = None


# Get the system arguments passed from the main engine
if len(sys.argv) > 1:
    data = sys.argv
else:
    data = None

if data and len(data) > 1:
    raw_data = json.loads(data[1])
    skeleton_root = raw_data['skeleton_root']
    file_list = ast.literal_eval(raw_data['data'])
    angle = raw_data['angle']
    mayapy = raw_data['mayapy']
    print('skeleton_root: %s' % skeleton_root)
    for x, y in dict(file_list).items():
        print(x, y)
    print(angle)
    print(mayapy)

    if 'bin' in mayapy:
        maya_root = mayapy.split('bin')[0]
    else:
        maya_root = ''

    # Import the maya plugins
    fbx_plugin_path = os.path.join(maya_root, "plug-ins/fbx/plug-ins/fbxmaya.mll")
    cmds.loadPlugin(fbx_plugin_path)

    # app = maya_playblaster()
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = queue_popup()
    window.show()


    # for _file, _path in dict(file_list).items():
    #     app.batch_process_fbx_playblasts(_path=os.path.join(_path, _file), _root=skeleton_root)

maya.standalone.uninitialize()
# if __name__ == '__main__':
#     start_path = 'C:/Users/sleep/OneDrive/Documents/Scripts/Python/Utilities/FBX_Editor/raw_data'
#     root = 'Reference'
#     batch_process_fbx_playblasts(_path=start_path, _root=root)

#     # build_maya_scene(_path='C:/Users/sleep/OneDrive/Documents/Scripts/Python/Utilities/FBX_Editor/raw_data/Run_Adam_001_006_Adam_Sneakers.fbx', root='Reference')
#     fbx_to_playblast()

# Command Line setup
# command = 'python("C:/Users/sleep/OneDrive/Documents/Scripts/Python/Utilities/FBX_Editor/fbx_playblaster.py")'

