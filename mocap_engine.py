# from maya import cmds
import pprint
import os
import sys
import re
import glob
import subprocess
import logging
from logging.handlers import TimedRotatingFileHandler
import ConfigParser

# -----------------------------------------------------------------------------------------------------
# Build Configuration
# -----------------------------------------------------------------------------------------------------
# Get the configuration file, parse it, combine it with the system path and then open it.
config = ConfigParser.ConfigParser()
sys_path = sys.path[0]
config_path = os.path.join(sys_path, 'devilsroto_config.cfg')
config.read(config_path)

# ------------------------------------------------------------------------------------------------------
# Create logging system
# ------------------------------------------------------------------------------------------------------
# Set the name of the log file and set it to the current path
log_file = 'devils_rotoscope_editor.log'
log_root = os.path.join(sys.path[0], 'logs')
# Build out folders if they do not already exist
if not os.path.exists(log_root):
    os.makedirs(log_root)
# Create the log path
log_path = os.path.join(log_root, log_file)
# Get the debugging settings from the configuration file and set the logging level appropriately
debug = config.get('Logging', 'debug_logging')
if debug == 'True' or debug == 'true' or debug == True:
    level = logging.DEBUG
else:
    level = logging.INFO

# Get the logger and set it's logging level
logger = logging.getLogger('devils_rotoscope')
logger.setLevel(level=level)
# Setup the timed rotating file handler with formatting
fh = TimedRotatingFileHandler(log_path, when='%s' % config.get('Logging', 'log_interval'), interval=1,
                              backupCount=int(config.get('Logging', 'log_days')))
fm = logging.Formatter(fmt='%(asctime)s - %(name)s | %(levelname)s : %(lineno)d - %(message)s')
fh.setFormatter(fm)
logger.addHandler(fh)

logger.info('Devil\'s Rotoscope Mocap Editor has started!')


class devils_roto(object):
    """
    This is the main engine for the Mocap Pipeline system.  It contains the following tools:
    export_edit: This tool trims and FBX file and puts it into proper project folder
    get_batch: Tries to find the mayabatch command
    """
    def __init__(self, parent=None):
        # Get configuration parameters
        self.mayabatch = config.get('Maya', 'batch_path')
        # Check for the existence of MayaBatch.exe by running get_batch()
        if not self.get_batch():
            no_batch_msg = 'Can\'t find Maya Batch.  Aborting.'
            logger.error(no_batch_msg)
            raise Exception(no_batch_msg)

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
                    search_path = os.path.join(root, f).replace('\\', '/')
                    find = re.findall(pattern.lower(), search_path.lower())
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

    def write_configuration(self, batch_path=None):
        # TODO: Eventually this will write out new configuration settings if needed.
        pass

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


if __name__ == '__main__':
    test = devils_roto()
    o_path = 'Q:/TLR/TLR100/Footage/mocap/06122020/TLR100_006_010/fbx_raw_exports'
    original_fbx = os.path.join(o_path, 'Grant_Red-002#Eric.fbx')
    output_name = 'TLR100_006_010_redGrant_take_002'
    test.export_edit(start_time=144, end_time=351, original_fbx=original_fbx, edit_name=output_name)
