__author__ = "Frank Vayssettes"
__maintainer__ = "Frank Vayssettes"
__status__ = "Beta"


import os, sys
#from PySide2 import QtUiTools, QtWidgets, QFileDialog
#from PySide2 import QtGui
from PySide6 import QtUiTools,QtCore,QtGui,QtWidgets
from PySide6.QtWidgets import (QApplication,QDockWidget,QPushButton,QHBoxLayout,QListWidgetItem,QFileDialog)
import inspect
import Lib.MKG_Lib as H



class Make_Grid():
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


        self.ui.bt_srcfolder.clicked.connect(self._srcfolder)
        self.ui.bt_ouputimg.clicked.connect(self._ouputimg)
        
        self.ui.bt_mkgrid.clicked.connect(self.mkgrid)

        self.ui.bt_srcfolder_2.clicked.connect(self._srcfolder_2)
        self.ui.bt_compress.clicked.connect(self._compress)

        #--Lock windows size
        w = self.ui.geometry().width()
        h = self.ui.geometry().height()
        self.ui.setFixedSize(w,h)
        self.ui.show()
        sys.exit(app.exec())


    def _srcfolder(self):
        folder = QFileDialog.getExistingDirectory(None, 'Select an awesome directory', "")
        if folder:
            self.ui.lineEdit_srcfolder.setText(folder)

    def _ouputimg(self):
        filenames, _ = QFileDialog.getSaveFileName(
                        None,
                        "QFileDialog.getSaveFileName()",
                        "",
                        "jpeg (*.jpg)",
                    )

        if filenames:
            self.ui.lineEdit_ouputimg.setText(filenames)


    def mkgrid(self):
        boxart_fold     = str(self.ui.lineEdit_srcfolder.text())#r"F:\Boxart_Project\Batocera_Systems\3do" ## path where the boxart images are stored
        output_img      = str(self.ui.lineEdit_ouputimg.text())#r"F:\Boxart_Project\result.jpg" ## the output file

        if not os.path.exists(boxart_fold):
            H.popup("Source folder does not exist")
        else:
            color_scale         = float( self.ui.doubleSpinBox_Color.value() ) #1.2 ## enhancement value
            only_compat_ratio   = True ## Try to use only cross compatible aspect ratios
            resolution          = ( int(self.ui.spinBox_Width.value()) , int(self.ui.spinBox_Height.value())   )#(1920,1080) ## output resolution
            ncol                = int(self.ui.spinBox_numberofcol.value()) #10 ## nuber of columns
            padding             = int(self.ui.spinBox_Padding.value()) #<5 ## spacing between boxarts


            res, llog = H.main_grid_creator(boxart_fold, resolution, ncol, padding, output_img, only_compat_aspectratio= only_compat_ratio, color_scale = color_scale)
            if res:
                strlog = "Done:\n"
                for l in llog:
                    strlog += "{}\n".format(l)
                
                H.popup(strlog)
            else:
                strlog = "Done:\n"
                for l in llog:
                    strlog += "{}\n".format(l)
                H.popup(strlog)

    def _srcfolder_2(self):
        folder = QFileDialog.getExistingDirectory(None, 'Select an awesome directory', "")
        if folder:
            self.ui.lineEdit_srcfolder_2.setText(folder)

    def _compress(self):
        boxart_fold     = str(self.ui.lineEdit_srcfolder_2.text())
        #H.popup( boxart_fold )
        if os.path.exists( boxart_fold ):
            imq = int(self.ui.spinBox_compression.value())
            hmax = int(self.ui.spinBox_Height_2.value())
            res = H.compress_boxart( boxart_fold, img_quality = imq, base_height = hmax )
            H.popup("Result:\n{}".format(res) )

t = Make_Grid()
