# -*- coding: utf-8 -*-
"""
Created on Tue May 18 11:12:33 2021

@author: Jan Family
"""

from SplashScreen  import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, qGray, QImage, QPainter, QPalette,QIcon
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
progressVal = 0
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
      
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.appProgress)
        self.timer.start(100)
        
        self.show()
        
    def appProgress(self):
        global progressVal
        global app
        self.ui.progressBar.setValue(progressVal)
        
        if progressVal >100:
            self.timer.stop()
            
            import sys
            from Main_ui import Window
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.WindowText, Qt.white)
            palette.setColor(QPalette.Base, QColor(25, 25, 25))
            palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            palette.setColor(QPalette.ToolTipBase, Qt.white)
            palette.setColor(QPalette.ToolTipText, Qt.white)
            palette.setColor(QPalette.Text, Qt.white)
            palette.setColor(QPalette.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ButtonText, Qt.white)
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Link, QColor(42, 130, 218))
            palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.HighlightedText, Qt.black)
        
        
        
            app.setApplicationName("Quick Crciket")
            app.setStyle("Fusion")
            
            
            
            app.setWindowIcon(QIcon('./Images/cricket.png'))
            app.setPalette(palette)
            self.widget= QtWidgets.QStackedWidget()
            main_window = Window(self.widget, "")
            self.widget.setFixedHeight(500)
            self.widget.setFixedWidth(1000)
            self.widget.addWidget(main_window)
            self.widget.setCurrentIndex(self.widget.currentIndex()+1)
            self.widget.show()
            self.close()
        progressVal+=5
if __name__ == "__main__":
    import sys
    global app
    
      
    import ctypes
    myappid = u'MiniDevloper21.Quick Crciket.Highlights.1.0' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
    
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    



 