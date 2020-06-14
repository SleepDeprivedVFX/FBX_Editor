from maya import cmds
import os
import pprint


new_file = cmds.file(new=True, f=True)
fbx_filepath = 'C:/Users/sleep/OneDrive/Documents/Scripts/Python/Utilities/FBX_Editor/raw_data/'
fbx_filename = 'Run_Adam_001_006_Adam_Sneakers.fbx'
fbx_file = os.path.join(fbx_filepath, fbx_filename)
fbx = cmds.file(fbx_file, i=True, applyTo=':')
cmds.select('Reference', r=True)
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


