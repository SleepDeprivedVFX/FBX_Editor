# from maya import cmds
import pprint
import os
import sys
import re
import glob
import subprocess
import logging
import configparser

# Create the logging system
logger = logging.getLevelName('devils_rotoscope')


class devils_roto(object):
    def __init__(self, parent=None):
        # Get configuration parameters
        self.config = configparser.ConfigParser()
        sys_path = sys.path[0]
        config_path = os.path.join(sys_path, 'devilsroto_config.cfg')
        self.config.read(config_path)
        self.mayabatch = self.config.get('Maya', 'batch_path')
        if not self.get_batch():
            print('Can\'t find Maya Batch.  Aborting.')

    def get_batch(self):
        '''
        This routine checks for the existence of the mayaBatch.exe.  If the one in the config file can't be found, it
        will try to find it from common paths.
        :return:  True if the the mayaBatch is good.  False if no mayabatch.exe can be found.
        '''
        print(self.mayabatch)

        # Check it's existence
        mb_exists = os.path.exists(self.mayabatch)
        if mb_exists:
            print(True)
            return True
        else:
            # Set OS platform variables.
            if sys.platform == 'win32':
                pattern = r'C:/Program Files/Autodesk/Maya\d+/bin/mayabatch.exe'
                app_path = os.walk('C:/Program Files/Autodesk')
            elif sys.platform == 'darwin':
                pattern = r'/Applications/Autodesk/maya\d+/Maya.app/Contents/bin/mayabatch'
                app_path = os.walk('/Applications/Autodesk')
            else:
                pattern = r'/usr/autodesk/maya\d+-x64/bin/mayabatch'
                app_path = os.walk('/usr/autodesk')

            # Check through the paths for a possible match
            found_paths = []
            for root, dirs, files in app_path:
                for f in files:
                    if f.endswith('.exe'):
                        search_path = os.path.join(root, f).replace('\\', '/')
                        find = re.findall(pattern.lower(), search_path.lower())
                        if find:
                            found_paths.append(find[0])
                            break
            if found_paths:
                found_paths = sorted(found_paths, reverse=True)
                print(found_paths)
            print(False)
            return False

    def export_edit(self, start_time=None, end_time=None, original_fbx=None, edit_name=None):
        print('original_fbx type: %s' % type(original_fbx))
        print('start_time type: %s' % type(start_time))
        print('end_time type: %s' % type(end_time))
        if original_fbx and type(original_fbx) == str:
            original_fbx = original_fbx.replace('\\', '/')
            if os.path.exists(original_fbx):
                print('Path exists: %s' % original_fbx)
                if type(start_time) in [float, int] and type(end_time) in [float, int]:
                    print('Numbers check out.')
                    if start_time and end_time:
                        pprint.pprint('exporting....')
                        with open(original_fbx, 'rb') as fbx:
                            print(fbx)
                            # TODO: Add the functionality to open the FBX in a command line and then export it out with
                            #       a new frame range, to a sepecific place on the server I'll need to get the specific
                            #       place from Asset Manager, or some other contextural organizer.

                        # Try to find the Maya batch file

            else:
                pprint.pprint('The FBX is non-existent.')
        else:
            pprint.pprint('The FBX is non-existent or is the wrong file type.')


if __name__ == '__main__':
    test = devils_roto()
    o_path = r'C:\Users\abenson\Documents\scripts\python\utilities\devilsroto_mocaptools\test_resources'
    original_fbx = os.path.join(o_path, 'mqhf_pre2_sc01-004.fbx')
    test.export_edit(start_time=1, end_time=120.12, original_fbx=original_fbx)
