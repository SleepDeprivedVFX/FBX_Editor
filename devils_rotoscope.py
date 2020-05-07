from maya import cmds
import pprint
import os
import subprocess


class devils_roto(object):
    def __init__(self, parent=None):
        pass
        
    def export_edit(self, start_time=None, end_time=None, original_fbx=None, edit_name=None):
        print(type(original_fbx))
        if original_fbx and type(original_fbx) == str:
            original_fbx = original_fbx.replace('\\', '/')
            if os.path.exists(original_fbx):
                if type(start_time) == float or type(start_time) == int and type(end_time) == float or type(end_time) == int:
                    print('Numvers check out.')
                    if start_time and end_time:
                        pprint.pprint('exporting....')
                        with open(original_fbx, 'rb') as fbx:
                            print(fbx)
                            # TODO: Add the functionality to open the FBX in a command line and then export it out with a new frame range, to a 
                            #       sepecific place on the server
                            #       I'll need to get the specific place from Asset Manager, or some other contextural organizer.
        else:
            pprint.pprint('The FBX is non-existent or is the wrong file type.')
                

if __name__ == '__main__':
    test = devils_roto()
    original_fbx = r'C:\Users\sleep\OneDrive\Documents\sg_jobs\Conan\anims\combine_anim_2.fbx'
    test.export_edit(start_time=1, end_time=120.12, original_fbx=original_fbx)
