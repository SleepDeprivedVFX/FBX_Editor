from maya import cmds
import math

        # fov = math.degrees(2 * math.atan(horizontalAperture_mm / (focalLength * 2)))

cmds.select('shot_cam')
cam = cmds.ls(sl=True)
cam_shape = cmds.listRelatives(s=True)
cam_horizontalAperture = cmds.getAttr('%s.horizontalFilmAperture' % cam_shape[0])
aperture_mm = 2.54 * cam_horizontalAperture * 10
focalLength = cmds.getAttr('%s.focalLength' % cam_shape[0])
fov = math.degrees(2 * math.atan(aperture_mm / (focalLength * 2)))
print('FOV: %s' % fov)

cmds.select('Reference', r=True)
obj = cmds.ls(sl=True)
print(obj)

bb = cmds.xform(bb=True, q=True)
print(bb)

x_min = bb[0]
y_min = bb[1]
z_min = bb[2]
x_max = bb[3]
y_max = bb[4]
z_max = bb[5]
center_x = x_min - ((x_min - x_max) / 2)
center_y = y_min - ((y_min - y_max) / 2)
center_z = z_min - ((z_min - z_max) / 2)

cube_diff = math.pow((x_max - x_min), 3) + math.pow((y_max - y_min), 3) + math.pow((z_max - z_min), 3)
obj_height = cube_diff ** (1. / 3.)

opposite = obj_height * 1.3

other_angle = 90 - fov
dist = math.tan(fov) * opposite
new_center_z = center_z + dist
cmds.xform(cam, translation=[center_x, center_y, new_center_z])

