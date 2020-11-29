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
import json
import logging
from logging.handlers import TimedRotatingFileHandler
from PySide2 import QtWidgets, QtCore, QtGui, QtUiTools
from ui import ui_devilsRoto_ui as dr

# Import tool bin
# from bin import fbx_playblaster as fbx_pb
# from bin import fbx_editor as fbx_ed

# Check the python version and import appropriately
try:
    if sys.version_info[0] >= 3:
        import configparser as ConfigParser
    else:
        import ConfigParser
except Exception as e:
    print('ConfigParser failed: %s' % e)

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

logger.info('Setting default Mocap settings...')
default_root_name = config.get('Mocap', 'default_root_name')


class devils_roto_ui(QtWidgets.QWidget):
    """
    The main Time Lord UI.
    """
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # --------------------------------------------------------------------------------------------------------
        # Set the saved settings
        # --------------------------------------------------------------------------------------------------------
        # This saves all the last settings so that they return to their previous state when the program is run again.
        self.settings = QtCore.QSettings(__author__, 'DevilsRoto')
        self.saved_pb_proc_batch = self.settings.value('pb_proc_batch', '.')
        self.saved_pb_proc_file = self.settings.value('pb_proc_file', '.')
        self.saved_pb_path = self.settings.value('pb_path', '.')
        self.saved_pb_origin_angle = self.settings.value('pb_origin_angle', '.')
        self.saved_ex_proc_batch = self.settings.value('ex_proc_batch', '.')
        self.saved_ex_proc_file = self.settings.value('ex_proc_file', '.')
        self.saved_ex_path = self.settings.value('ex_path', '.')
        self.saved_tab = self.settings.value('tabs', '0')
        self.saved_window_position = self.settings.value('geometry')
        self.restoreGeometry(self.saved_window_position)

        # --------------------------------------------------------------------------------------------------------
        # Setup UI
        # --------------------------------------------------------------------------------------------------------
        self.ui = dr.Ui_DevilsRotoscope()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icons/dr_icon.png'))
        self.setWindowTitle("Devil's Rotoscope v%s" % __version__)
        # self.set_window_on_top()
        self.ui.pb_cancel_btn.clicked.connect(self.close)
        self.ui.ex_cancel_btn.clicked.connect(self.close)
        self.ui.cfg_cancel_btn.clicked.connect(self.close)
        self.ui.pb_browse_btn.clicked.connect(lambda: self.get_folder_file(field=self.ui.pb_folder_file,
                                                                           type=self.ui.pb_batch_btn.isChecked(),
                                                                           ext='FBX(*.fbx)'))
        self.ui.ex_browse_btn.clicked.connect(lambda: self.get_folder_file(field=self.ui.ex_folder_file,
                                                                           type=self.ui.ex_batch_btn.isChecked(),
                                                                           ext='FBX(*.fbx)'))
        self.ui.cfg_mayabatch_btn.clicked.connect(lambda: self.get_folder_file(field=self.ui.cfg_maya_batch_path,
                                                                               type=False, ext='EXE(*.exe)'))
        self.ui.cfg_mayapy_btn.clicked.connect(lambda: self.get_folder_file(field=self.ui.cfg_mayapy_path,
                                                                            type=False, ext='EXE(*.exe)'))
        self.ui.cfg_maya_batch_path.setText(config.get('Maya', 'batch_path'))
        self.ui.cfg_mayapy_path.setText(config.get('Maya', 'mayapy_path'))
        if config.get('Logging', 'debug_logging') == 'True':
            self.ui.cfg_debug_logging.setChecked(True)
        else:
            self.ui.cfg_debug_logging.setChecked(False)
        self.ui.cfg_num_days_logging.setValue(int(config.get('Logging', 'log_days')))
        self.ui.cfg_default_root.setText(config.get('Mocap', 'default_root_name'))

        # Setup button connections
        self.ui.pb_run_btn.clicked.connect(self.run_playblast)
        self.ui.pb_queue_btn.clicked.connect(lambda: self.load_queue(path_obj=self.ui.pb_folder_file,
                                                                     batch=self.ui.pb_batch_btn.isChecked()))

        # ---------------------------------------------------------------------------------------------------------
        # Set the default values from saved settings
        # ---------------------------------------------------------------------------------------------------------
        if self.saved_pb_proc_batch == 'true' or self.saved_pb_proc_batch == True:
            self.saved_pb_proc_batch = True
        else:
            self.saved_pb_proc_batch = False
        if self.saved_pb_proc_file == 'true' or self.saved_pb_proc_file == True:
            self.saved_pb_proc_file = True
        else:
            self.saved_pb_proc_file = False
        if self.saved_ex_proc_batch == 'true' or self.saved_ex_proc_batch == True:
            self.saved_ex_proc_batch = True
        else:
            self.saved_ex_proc_batch = False
        if self.saved_ex_proc_file == 'true' or self.saved_ex_proc_file == True:
            self.saved_ex_proc_file = True
        else:
            self.saved_ex_proc_file = False
        if not self.saved_tab:
            self.saved_tab = 0
        self.ui.pb_batch_btn.setChecked(self.saved_pb_proc_batch)
        self.ui.pb_file_btn.setChecked(self.saved_pb_proc_file)
        self.ui.pb_folder_file.setText(self.saved_pb_path)
        if self.saved_pb_origin_angle:
            self.ui.pb_origin_angle.setValue(float(self.saved_pb_origin_angle))
        self.ui.ex_batch_btn.setChecked(self.saved_ex_proc_batch)
        self.ui.ex_file_btn.setChecked(self.saved_ex_proc_file)
        self.ui.ex_folder_file.setText(self.saved_ex_path)
        self.ui.toolboxes.setCurrentIndex(int(self.saved_tab))

        # SETUP ENGINE
        # self.devils_roto = devils_roto()
        header = self.ui.pb_queue.horizontalHeader()
        self.ui.pb_queue.setHorizontalHeaderLabels(['X', 'Filename', 'Path'])
        # TODO: I need to get the resize to contents working.  It does not currently
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def load_queue(self, path_obj=None, batch=True):
        """
        This will load the queue from either a folder or a file, depending on the batch or file settings and the
        existence of an actual file or folder.
        :return:
        """
        fbx_files = []
        if path_obj:
            path = path_obj.text()
            if os.path.exists(path):
                if batch:
                    if os.path.isfile(path):
                        path = os.path.dirname(path)
                        self.update_folder_file(field=path_obj, string=path)
                    all_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
                    for f in all_files:
                        if f.endswith('.fbx'):
                            fbx_files.append(os.path.join(path, f))
                else:
                    if not os.path.isfile(path):
                        print('Path_obj: %s' % path_obj)
                        print('batch: %s' % batch)
                        self.get_folder_file(field=path_obj, type=batch, ext='FBX(*.fbx)')
                        path = path_obj.text()
                    if path.endswith('.fbx'):
                        fbx_files.append(path)
                    else:
                        print('Could not get file object')
            print('fbx_files: %s' % fbx_files)
            if fbx_files:
                self.ui.pb_queue.clear()
                self.ui.pb_queue.setRowCount(0)
                header = self.ui.pb_queue.horizontalHeader()
                self.ui.pb_queue.setHorizontalHeaderLabels(['X', 'Filename', 'Path'])
                # TODO: Set the tool tips for the headers
                #  u"<html><head/><body><p><span style=\" font-weight:600; color:#0c0c0c;\">
                #  Export (X)</span></p><p><span style=\" color:#0c0c0c;\">When checked, the
                #  file will be processed.</span></p></body></html>", None));

                # TODO: I need to get the resize to contents working.  It does not currently
                header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
                for fbx in fbx_files:
                    row = self.ui.pb_queue.rowCount()
                    filename = os.path.basename(fbx)
                    filepath = os.path.dirname(fbx)
                    self.ui.pb_queue.insertRow(row)
                    checkbox = QtWidgets.QTableWidgetItem()
                    checkbox.setCheckState(QtCore.Qt.Checked)
                    self.ui.pb_queue.setItem(row, 0, checkbox)
                    self.ui.pb_queue.setItem(row, 1, QtWidgets.QTableWidgetItem(filename))
                    self.ui.pb_queue.setItem(row, 2, QtWidgets.QTableWidgetItem(filepath))
                    self.ui.pb_queue.setRowHeight(row, 14)
                self.ui.pb_queue.insertRow(row + 1)

    def run_playblast(self):
        # This will launch the Maya Standalone Engine and run the playblaster.
        mayapy_path = self.ui.cfg_mayapy_path.text()
        skeleton_root = self.ui.cfg_default_root.text()
        angle = self.ui.pb_origin_angle.value()

        pb_count = self.ui.pb_queue.rowCount()
        pb_list = {}
        if pb_count > 0:
            for c in range(pb_count - 1):
                pb_list[self.ui.pb_queue.item(c, 1).text()] = self.ui.pb_queue.item(c, 2).text()

        print('pb_list: %s' % pb_list)
        print('skeleton_root: %s' % skeleton_root)
        data_raw = '{"skeleton_root": "%s", "data": "%s", "angle": "%s", "mayapy": "%s"}' % (skeleton_root, pb_list,
                                                                                             angle, mayapy_path)
        data = json.dumps(data_raw)
        local_path = os.path.dirname(sys.argv[0])
        run_path = os.path.join(local_path, 'bin/fbx_playblaster.py')
        if os.path.exists(mayapy_path):
            run_test = subprocess.Popen('%s %s %s' % (mayapy_path, run_path, data))
            print(run_test)

    def get_folder_file(self, field=None, type=None, ext=None):
        """
        This will return either a folder or a file depending on the type
        :param field: This takes the prefix that defines a particular tool tab to know where to return the path
        :param type: This takes in a boolean to determine whether to use folder or file type
        :return:
        """
        if field:
            if type:
                browse = QtWidgets.QFileDialog.getExistingDirectory(caption='Select Folder', dir=field.text())
                if browse:
                    field.setText(browse)
            else:
                browse = QtWidgets.QFileDialog.getOpenFileName(caption='Select File',
                                                               dir=os.path.dirname(field.text()),
                                                               filter=ext)[0]
                if browse:
                    field.setText(browse)

    def update_folder_file(self, field=None, string=None):
        if field and string:
            field.setText(string)

    def update_saved_settings(self):
        """
        The settings that are saved after the window is closed.  These consist of fields and form data that a user micht
        prefer to remain consistent whenever the tool is used. This includes window position and size, and each of the
        various settings for a given tool.
        The Configuration Data is always read directly from the Config file and is not saved on the system.
        :return:
        """
        self.settings.setValue('pb_proc_batch', self.ui.pb_batch_btn.isChecked())
        self.settings.setValue('pb_proc_file', self.ui.pb_file_btn.isChecked())
        self.settings.setValue('pb_path', self.ui.pb_folder_file.text())
        self.settings.setValue('pb_origin_angle', self.ui.pb_origin_angle.value())
        self.settings.setValue('ex_proc_batch', self.ui.ex_batch_btn.isChecked())
        self.settings.setValue('ex_proc_file', self.ui.ex_file_btn.isChecked())
        self.settings.setValue('ex_path', self.ui.ex_folder_file.text())
        self.settings.setValue('tabs', self.ui.toolboxes.currentIndex())
        self.settings.setValue('geometry', self.saveGeometry())

        self.saved_pb_proc_batch = self.ui.pb_batch_btn.isChecked()
        self.saved_pb_proc_file = self.ui.pb_file_btn.isChecked()
        self.saved_pb_path = self.ui.pb_folder_file.text()
        self.saved_ex_proc_batch = self.ui.ex_batch_btn.isChecked()
        self.saved_ex_proc_file = self.ui.ex_file_btn.isChecked()
        self.saved_ex_path = self.ui.ex_folder_file.text()
        self.saved_pb_origin_angle = self.ui.pb_origin_angle.value()

    def closeEvent(self, event):
        self.update_saved_settings()


if __name__ == '__main__':
    # test = devils_roto()
    o_path = 'C:/Users/sleep/OneDrive/Documents/Scripts/Python/Utilities/FBX_Editor/raw_data/output/'
    original_fbx = os.path.join(o_path, 'Cut_a_Fart.fbx')
    output_name = 'Cut_a_Fart'
    # test.export_edit(start_time=144, end_time=351, original_fbx=original_fbx, edit_name=output_name)

    # -------------------------------------------------------------------
    # Test Getting the First Frame
    # -------------------------------------------------------------------
    # cmds.file(new=True)
    # cmds.loadPlugin('fbxmaya')
    # cmds.file(original_fbx, i=True)
    # cmds.select(default_root_name, r=True)
    # dr = devils_roto()
    # dr.get_first_frame()

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app.setOrganizationName('AdamBenson')
    app.setOrganizationDomain('adamdbenson.com')
    app.setApplicationName('DevilsRoto')
    splash_pix = QtGui.QPixmap('ui/resources/devils_roto_logo.png')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    window = devils_roto_ui()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
