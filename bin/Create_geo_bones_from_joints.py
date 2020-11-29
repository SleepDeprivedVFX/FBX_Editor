from maya import cmds
import math

# Create geo bones from joints

joints = cmds.ls(type='joint')

print(joints)
id = 1

joint_data = {}
for joint in joints:
    children = cmds.listRelatives(joint, c=True)
    if children and len(children) >= 1:
        joint_data[joint] = {
            'children': children
        }

# This will need a way to determine varying joint hierarchies!  Spine to arms to legs, et cetera.
for joint, data in joint_data.items():
    print('-' * 100)
    print(joint)
    print(id)
    j_children = data['children']
    print(j_children)
    j_radius = cmds.getAttr('%s.radius' % joint)
    print('radius:', j_radius)
    for child in j_children:
        j_pos = cmds.xform(joint, q=True, t=True, ws=True)
        c_pos = cmds.xform(child, q=True, t=True, ws=True)
        print(j_pos)
        print('position:', j_pos)
        j_orient = cmds.getAttr('%s.jointOrient' % joint)
        print('orientation:', j_orient)
        half_rad = j_radius / 2
        
        # Find the distance to the next joint
        distance = math.sqrt(((c_pos[0] - j_pos[0]) ** 2) + ((c_pos[1] - j_pos[1]) ** 2) + ((c_pos[2] - j_pos[2]) ** 2))
        # distance = cmds.distanceDimension(sp=j_pos, ep=c_pos)
        print('distance:', distance)
        # height = cmds.getAttr('%s.distance' % distance)
        height = distance
        print('height:', height)
        # cmds.delete(distance)
        
        new_cube = cmds.polyCube(h=half_rad, d=half_rad, w=height,  n='%s_bone' % joint)
        new_piv_dist = 0.0 - (height / 2.0)
        cmds.xform(new_cube, piv=(new_piv_dist, 0.0, 0.0))
        point = cmds.pointConstraint(joint, new_cube, mo=False)
        aim = cmds.aimConstraint(child, new_cube)
        cmds.delete(point)
        cmds.delete(aim)
        cmds.parentConstraint(joint, new_cube, mo=True)
