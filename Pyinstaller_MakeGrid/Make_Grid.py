__author__ = "Frank Vayssettes"
__maintainer__ = "Frank Vayssettes"
__email__ = "frank.v7@mocaplab.com"
__status__ = "Beta"


import os, sys
from PySide2 import QtUiTools, QtWidgets
from PySide2 import QtGui
import inspect
import Lib.Demo_Lib as H



class C3D_Checker():
    '''
    '''
    toolname = "Make Grid"
    version = 0.01
    curPath = os.path.dirname(sys.argv[0]).replace("/", "\\")

    def __init__(self):
        # --UI
        app = QtWidgets.QApplication(sys.argv)

        MAIN_PATH_SCRIPT    = inspect.getsourcefile(lambda:None)
        MAIN_DIR_SCRIPT, FILE_SCRIPT = os.path.split(MAIN_PATH_SCRIPT)


        relPath     = os.path.join( MAIN_DIR_SCRIPT, "Lib\\Demo.ui")
        appIco      = os.path.join( MAIN_DIR_SCRIPT, "Lib\\MCL.ico")


        app.setWindowIcon(QtGui.QIcon(appIco))
        self.ui = QtUiTools.QUiLoader().load(relPath)
        self.ui.setWindowTitle(self.toolname + " v" + str(self.version))


        self.ui.bt_yay.clicked.connect(self.yay)


        #--Lock windows size
        w = self.ui.geometry().width()
        h = self.ui.geometry().height()
        self.ui.setFixedSize(w,h)
        self.ui.show()
        sys.exit(app.exec_())

    def yay(self):
        boxart_fold     = r"F:\Boxart_Project\Batocera_Systems\3do" ## path where the boxart images are stored
        output_img      = r"F:\Boxart_Project\result.jpg" ## the output file

        color_scale         = 1.2 ## enhancement value
        only_compat_ratio   = True ## Try to use only cross compatible aspect ratios
        resolution          = (1920,1080) ## output resolution
        ncol                = 10 ## nuber of columns
        padding             = 5 ## spacing between boxarts

        H.main_grid_creator(boxart_fold, resolution, ncol, padding, output_img, only_compat_aspectratio= only_compat_ratio, color_scale = color_scale)
        H.popup("Yay")



t = C3D_Checker()
