from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QLabel,QWidget,QApplication,QProgressBar,QVBoxLayout,QDialog,QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore  import *
from FramesExtraction import FramesExtractor

class SetSpanWindow(QMainWindow):
    
    def __init__(self,widget,FilePath):
        self.file = str('./Frames')
        
        self.widget = widget
        self.FilePath = FilePath
        self.framePath = self.file
 
        super(SetSpanWindow,self).__init__()
        loadUi("./Ui_s/SetSpanUi.ui",self)
        self.button_connections()
        
    def button_connections(self):
        
        #Disable It after Gui Completition
        #self.btn_next.setEnabled(False)
        
        #Next Button
        self.btn_next.clicked.connect(lambda: self.btn_next_ftn())
        
        #Back Button
        self.btn_back.clicked.connect(lambda: self.btn_back_ftn())
        
        #Proceed Button
        self.btn_proceed.clicked.connect(lambda: self.btn_proceed_ftn())
        
        #Home Button
        self.btn_home.clicked.connect(lambda: self.btn_home_ftn())
    
    def btn_next_ftn(self):
        from SelectImageUi import SelectImageWindow
        select_img_win = SelectImageWindow(self.widget,self.framePath,self.FilePath)
        self.widget.addWidget(select_img_win)
        self.widget.setFixedHeight(375)
        self.widget.setFixedWidth(872)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

  
    def btn_back_ftn(self):
        import sys
        from Main_ui import Window
        main_window = Window(self.widget, self.FilePath)
        self.widget.addWidget(main_window)
        self.widget.setFixedHeight(500)
        self.widget.setFixedWidth(1000)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
    def btn_home_ftn(self):
        import sys
        from Main_ui import Window
        main_window = Window(self.widget, self.FilePath)
        self.widget.addWidget(main_window)
        self.widget.setFixedHeight(500)
        self.widget.setFixedWidth(1000)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
    def btn_proceed_ftn(self):
        import os
        import shutil
        try:
            if os.path.exists(self.file):
                shutil.rmtree(self.file)
            os.mkdir(self.file)
            self.SetFramesPath=self.file
            print(self.SetFramesPath)
        except OSError as e:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("File not found")
            msg.setWindowTitle("Error")
            msg.exec_()
        
        span=int(self.span_comboBox.currentText())

        # print(type(span))
        import cv2
        cap= cv2.VideoCapture(self.FilePath)
        framespersecond= int(cap.get(cv2.CAP_PROP_FPS))
        TotalVideoLength=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # print("The total number of frames in this video is ", framespersecond)
        # print("The total number of seconds in this video is ", TotalVideoLength)
        total=0
        if framespersecond <25:
            self.thread = FramesExtractor(self,cap,total,span,TotalVideoLength,self.SetFramesPath,framespersecond)
            self.thread.start()
            self.thread.change_value.connect(self.updateProgressBar)
            self.Frame_Label.setText('Stroring Frames in Directory....')
            self.thread.finished.connect(self.onComplete)

            #Enable When you Comaplte the Gui
            #self.btn_next.setEnabled(True)
            
        elif framespersecond >=25 and framespersecond <=30:
            self.thread = FramesExtractor(self,cap,total,span,TotalVideoLength,self.SetFramesPath,framespersecond)
            self.thread.start()
            self.thread.change_value.connect(self.updateProgressBar)
            self.Frame_Label.setText('Stroring Frames in Directory....')
            self.thread.finished.connect(self.onComplete)

            #Enable When you Comaplte the Gui
            #self.btn_next.setEnabled(True)
            
        elif framespersecond >30 and framespersecond<=40:
            self.thread = FramesExtractor(self,cap,total,span,TotalVideoLength,self.SetFramesPath,framespersecond)
            self.thread.start()
            self.thread.change_value.connect(self.updateProgressBar)
            self.Frame_Label.setText('Stroring Frames in Directory....')
            self.thread.finished.connect(self.onComplete)
 
            #Enable When you Comaplte the Gui
            #self.btn_next.setEnabled(True)
            
        else:
            self.thread = FramesExtractor(self,cap,total,span,TotalVideoLength,self.SetFramesPath,framespersecond)
            self.thread.start()
            self.thread.change_value.connect(self.updateProgressBar)
            self.Frame_Label.setText('Stroring Frames in Directory....')
            self.thread.finished.connect(self.onComplete)
            
            #Enable When you Comaplte the Gui
            #self.btn_next.setEnabled(True)
            
        
    def updateProgressBar(self,val):
        self.progBar.setValue(val)
    def onComplete(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Frames Excuted SuccessFully")
        msg.setWindowTitle("Information")
        msg.exec_()
        self.Frame_Label.setText('Fames Saved Successfully....')
