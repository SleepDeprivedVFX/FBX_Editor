"""
Devils Rotoscope
Motion Capture Processing Toolkit
"""
__author__ = 'Adam Benson'
__version__ = '0.1.0'

# from maya import cmds
import pprint
import os
import sys
import re
import glob
import subprocess
import logging
from logging.handlers import TimedRotatingFileHandler
from PySide2 import QtWidgets, QtCore, QtGui
from ui import ui_devilsRoto_ui as dr

# Check the python version and import appropriately
try:
    if sys.version_info[0] >= 3:
        import configparser as ConfigParser
    else:
        import ConfigParser
except Exception as e:
    print('ConfigParser failed: %s' % e)


class devils_roto(object):
    """
    This is the main engine for the Mocap Pipeline system.  It contains the following tools:
    export_edit: This tool trims and FBX file and puts it into proper project folder
    get_batch: Tries to find the mayabatch command
    """
    def __init__(self, parent=None):
        # Get configuration parameters
        self.mayabatch = config.get('Maya', 'batch_path')
        self.mayapy = config.get('Maya', 'mayapy_path')
        # Check for the existence of MayaBatch.exe by running get_batch()
        if not self.get_batch():
            no_batch_msg = 'Can\'t find Maya Batch.  Aborting.'
            logger.error(no_batch_msg)
            raise Exception(no_batch_msg)
        if not self.get_mayapy():
            no_mayapy_msg = 'Can\'t find MayaPy.  Aborting.'
            logger.error(no_mayapy_msg)
            raise Exception(no_mayapy_msg)

    def get_batch(self):
        '''
        This routine checks for the existence of the mayaBatch.exe.  If the one in the config file can't be found, it
        will try to find it from common paths.
        :return:  True if the the mayaBatch is good.  False if no mayabatch.exe can be found.
        '''

        # Check mayabatch.exe's existence
        mb_exists = os.path.exists(self.mayabatch)
        if mb_exists:
            logger.info('MayaBatch is connected.')
            return True
        else:
            # Set OS platform variables.
            logger.info('MayaBatch was not found where the config file said it would be.  Searching...')
            if sys.platform == 'win32':
                batch_pattern = r'C:/Program Files/Autodesk/Maya\d+/bin/mayabatch.exe'
                app_path = os.walk('C:/Program Files/Autodesk')
            elif sys.platform == 'darwin':
                batch_pattern = r'/Applications/Autodesk/maya\d+/Maya.app/Contents/bin/mayabatch'
                app_path = os.walk('/Applications/Autodesk')
            else:
                batch_pattern = r'/usr/autodesk/maya\d+-x64/bin/mayabatch'
                app_path = os.walk('/usr/autodesk')

            # Check through the paths for a possible match
            found_paths = []
            for root, dirs, files in app_path:
                for f in files:
                    search_path = os.path.join(root, f).replace('\\', '/')
                    find = re.findall(batch_pattern.lower(), search_path.lower())
                    if find:
                        # A Maya Batch file was found!
                        logger.info('MayaBatch found!')
                        found_paths.append(find[0])
                        break

            if found_paths:
                # Get the latest version of MayaBatch.
                found_paths = sorted(found_paths, reverse=True)
                new_path = found_paths[0]

                # Set the Maya batch path and update the config file
                self.mayabatch = new_path
                if os.path.exists(self.mayabatch):
                    # TODO: Setup the config write feature
                    self.write_configuration(batch_path=self.mayabatch)
                    # config.set('Maya', 'batch_path', new_path)
                    # with open(config_path, 'w') as w_config:
                    #     # w_config.write(config)
                    #     print(config.get('Maya', 'batch_path'))
                    logger.info('MayaBatch is now connected.')
                    return True
            logger.error('Could not find the MayaBatch file!')
            return False

    def get_mayapy(self):
        '''
        This routine checks for the existence of the mayaBatch.exe.  If the one in the config file can't be found, it
        will try to find it from common paths.
        :return:  True if the the mayaBatch is good.  False if no mayabatch.exe can be found.
        '''

        # Check mayabatch.exe's existence
        mpy_exists = os.path.exists(self.mayapy)
        if mpy_exists:
            logger.info('MayaPy is connected.')
            return True
        else:
            # Set OS platform variables.
            logger.info('MayaPy was not found where the config file said it would be.  Searching...')
            if sys.platform == 'win32':
                py_pattern = r'C:/Program Files/Autodesk/Maya\d+/bin/mayapy.exe'
                app_path = os.walk('C:/Program Files/Autodesk')
            elif sys.platform == 'darwin':
                py_pattern = r'/Applications/Autodesk/Maya\d+/Maya.app/Contents/bin/mayapy.exe'
                app_path = os.walk('/Applications/Autodesk')
            else:
                py_pattern = r'/usr/autodesk/maya\d+-x64/bin/mayapy'
                app_path = os.walk('/usr/autodesk')

            # Check through the paths for a possible match
            found_paths = []
            found_py_paths = []
            for root, dirs, files in app_path:
                for f in files:
                    search_path = os.path.join(root, f).replace('\\', '/')
                    find_py = re.findall(py_pattern.lower(), search_path.lower())
                    t = False
                    if find_py:
                        # A Maya Py file was found!
                        logger.info('MayaPy found!')
                        found_py_paths.append(find_py[0])
                        break

            if found_py_paths:
                # Get the latest version of MayaPy
                found_py_paths = sorted(found_py_paths, reverse=True)
                new_py_path = found_py_paths[0]

                # Set the Maya py path and update the config file
                self.mayapy = new_py_path
                if os.path.exists(self.mayapy):
                    # TODO: Setup the config write feature
                    self.write_configuration(mayapy_path=self.mayapy)
                    # config.set('Maya', 'batch_path', new_path)
                    # with open(config_path, 'w') as w_config:
                    #     # w_config.write(config)
                    #     print(config.get('Maya', 'batch_path'))
                    logger.info('MayaPy is now connected.')
                    return True
            logger.error('Could not find the MayaPy file!')
            return False

    def write_configuration(self, batch_path=None, mayapy_path=None):
        # TODO: Eventually this will write out new configuration settings if needed.
        pass

    def get_path_from_context(self, data=None):
        # TODO: This routine needs to take minor information and get the relative path for a shot or asset.  For now
        #       it will simply return the data given to it
        output_path = None
        if data:
            output_path = data
        return output_path

    def get_first_frame(self):
        objs = cmds.ls(selection=True)
        for obj in objs:

            animAttributes = cmds.listAnimatable(obj);

            first_keyframe = 999999999

            for attribute in animAttributes:

                numKeyframes = cmds.keyframe(attribute, query=True,
                                             keyframeCount=True)

                if (numKeyframes > 0):
                    times = cmds.keyframe(attribute, query=True,
                                          index=(0, numKeyframes), timeChange=True)

                    for i in range(0, numKeyframes):
                        if times[i] < first_keyframe:
                            first_keyframe = times[i]
                        else:
                            continue
        print('First Keyframe: %s' % first_keyframe)

    def export_edit(self, start_time=None, end_time=None, original_fbx=None, edit_name=None, destination=None):
        logger.debug('original_fbx type: %s' % type(original_fbx))
        logger.debug('start_time type: %s' % type(start_time))
        logger.debug('end_time type: %s' % type(end_time))

        # Test if the call is valid
        if original_fbx and type(original_fbx) == str:
            # Cleanup the path separators
            original_fbx = original_fbx.replace('\\', '/')
            # Test for the files existence.
            if os.path.exists(original_fbx):
                # Setup inputs
                logger.debug('Path exists: %s' % original_fbx)
                orig_path = os.path.dirname(original_fbx)
                orig_file = os.path.basename(original_fbx)
                # Check for bad characters and replace them with underscores
                if '-' in orig_file:
                    orig_file = orig_file.replace('-', '_')
                if ' ' in orig_file:
                    orig_file = orig_file.replace(' ', '_')
                # Set the file name
                name = os.path.splitext(orig_file)[0]

                # Build Destination output
                if not destination:
                    # Default same folder export
                    destination = os.path.join(orig_path, 'output')
                # Build any non-existent folder structures
                if not os.path.exists(destination):
                    os.makedirs(destination)

                # The edit name is the name of the output FBX file.  If it is not supplied, then '_edited' is appended
                if edit_name:
                    output_file = '%s.fbx' % edit_name
                else:
                    output_file = '%s_edited.fbx' % name
                # Create the output file path
                output = os.path.join(destination, output_file)

                # Check frame range number and start processing.
                if type(start_time) in [float, int] and type(end_time) in [float, int]:
                    logger.debug('The frame numbers are valid.')
                    if start_time and end_time:
                        pprint.pprint('exporting....')
                        original_fbx = original_fbx.replace('\\', '/')
                        output = output.replace('\\', '/')
                        # TODO: This needs to move the new animation to frame 1001... somehow.
                        command = 'file -import -type \\"FBX\\" -ignoreVersion -ra true -mergeNamespacesOnClash false ' \
                                  '-rpr \\"%s\\" -options \\"fbx\\" -pr -importFrameRate true -importTimeRange ' \
                                  '"override" \\"%s\\";playbackOptions -min %f -max %f;' \
                                  'FBXExportSplitAnimationIntoTakes -v \\"%s\\" %f %f;FBXExport -f \\"%s\\";' % \
                                  (name, original_fbx, start_time, end_time, edit_name, start_time, end_time, output)
                        result = subprocess.call('%s -command "%s"' % (self.mayabatch, command))
                        print('RESULT: %s' % result)

            else:
                pprint.pprint('The FBX is non-existent.')
        else:
            pprint.pprint('The FBX is non-existent or is the wrong file type.')

