# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 23:25:59 2021

@author: Guiz
"""

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog,QLabel,QWidget,QApplication,QProgressBar,QVBoxLayout,QDialog,QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore  import *
import numpy as np 

class SelectImageWindow(QMainWindow):
    
    def __init__(self,widget,FramesPath,FilePath):
        self.widget = widget
        self.FramesPath = FramesPath
        self.FilePath = FilePath
        super(SelectImageWindow,self).__init__()
        loadUi("./Ui_s/SelectImage.ui",self)
        self.button_connections()
        
    def button_connections(self):
        print("done")
        #Next Button
        self.btn_next.setEnabled(True)
        self.btn_next.clicked.connect(lambda: self.btn_next_ftn())
        
         #Back Button
        self.btn_back.clicked.connect(lambda: self.btn_back_ftn())
        
         #Generate Image Button
        self.btn_gen_img.clicked.connect(lambda: self.generate_image())
        
        #Home Button
        self.btn_home.clicked.connect(lambda: self.btn_home_ftn())
    def btn_back_ftn(self):
        import SetSpanUi
        ui= SetSpanUi.SetSpanWindow(self.widget,self.FramesPath)
        self.widget.addWidget(ui)
        self.widget.setFixedHeight(375)
        self.widget.setFixedWidth(872)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
    def btn_next_ftn(self):
        import TextDetectionUi
        ui= TextDetectionUi.TextDetectionWindow(self.widget,self.FramesPath,self.ref_point,self.FilePath)
        self.widget.addWidget(ui)
        self.widget.setFixedHeight(375)
        self.widget.setFixedWidth(872)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
    def btn_home_ftn(self):
        import sys
        from Main_ui import Window
        main_window = Window(self.widget, self.FilePath)
        self.widget.addWidget(main_window)
        self.widget.setFixedHeight(500)
        self.widget.setFixedWidth(1000)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
    def generate_random_image(self):
        import os, random
        return self.FramesPath +"/"+ random.choice(os.listdir(self.FramesPath))
    def generate_image(self):
        print("gen butn")
        #Frames Selection Area
        # import the necessary packages
        import cv2
        from PIL import Image
        # initialize the list of reference points and boolean indicating
        # whether cropping is being performed or not
        ref_point = []
        cropping = False
        #For Scores Selection
        # load the image, clone it, and setup the mouse callback function
        self.image = cv2.imread(self.generate_random_image())  
        # font
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL    
        # fontScale
        fontScale = 1
        # white color in BGR
        color = (0, 0, 0)
        
        # Line thickness of 2 px
        thickness = 2
        #image=image[500:1900,0:1080]
        self.clone = self.image.copy()
        print("Called")
        cv2.namedWindow("image")
        def gen_buttons(image):
            global button1,button2,button3
            #Button 1 area 
            x1,y1,x2,y2 = 20,130,135,160
            #Button 2 area 
            x3,y3,x4,y4 = 20,180,120,210
            #Button 3 area 
            x5,y5,x6,y6 = 20,230,220,260
            
            #Button with text    
            #confirm button
            cv2.rectangle(image, (x1,y1), (x2,y2), (255,255,255), -1)
            cv2.putText(image, 'Confirm', (30 ,150), font, fontScale, color, thickness, cv2.LINE_AA)
            
            #Reset button
            cv2.rectangle(image, (x3, y3), (x4,y4), (255,255,255), -1)
            cv2.putText(image, 'Reset', (30 ,200), font, fontScale, color, thickness, cv2.LINE_AA)
           
            #Gererate Again button
            cv2.rectangle(image, (x5, y5), (x6,y6), (255,255,255), -1)
            cv2.putText(image, 'Generate Again', (30 ,250), font, fontScale, color, thickness, cv2.LINE_AA)
            
            button1 = [x1,y1,x2,y2]
            button2 = [x3,y3,x4,y4]
            button3 = [x5,y5,x6,y6]
        def shape_selection(event, x, y, flags, param):
          image = self.image
          # grab references to the global variables
          global ref_point, cropping
        
          # if the left mouse button was clicked, record the starting
          # (x, y) coordinates and indicate that cropping is being
          # performed
          if event == cv2.EVENT_LBUTTONDOWN:
            
            if x > button1[0] and x < button1[2] and y > button1[1] and y < button1[3]:   
                print('Confirm Button Called')
                if len(ref_point) == 2:
                  self.ref_point = ref_point
                  crop_img = self.clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
                  cv2.imshow("crop_img", crop_img)
                  msg = QtWidgets.QMessageBox()
                  msg.setIcon(QtWidgets.QMessageBox.Information)
                  msg.setText("Selection Successful")
                  msg.setWindowTitle("Information")
                  msg.exec_()
                  cv2.destroyAllWindows()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setText("Error: Select only score and wickets part.")
                    msg.setWindowTitle("Wrong Selection")
                    msg.exec_()
            elif x > button2[0] and x < button2[2] and y > button2[1] and y < button2[3]:   
                print('Reset Button Called')
                    
                ref_point = []
                cropping = False
                print(ref_point) 
                self.image= self.clone.copy()
                gen_buttons(self.image)
                cv2.imshow("image", self.image)
            elif x > button3[0] and x < button3[2] and y > button3[1] and y < button3[3]:  
                print('Generate Again button called')
                ref_point = []
                cropping = False
                print(ref_point) 
                self.image = cv2.imread(self.generate_random_image()) 
                self.clone = self.image.copy()
                gen_buttons(self.image)
                cv2.imshow("image", self.image) 
            else:
                ref_point = [(x, y)]
                cropping = True
                print("exec down")
        
          # check to see if the left mouse button was released
          elif event == cv2.EVENT_LBUTTONUP:
            if x > button1[0] and x < button1[2] and y > button1[1] and y < button1[3]:
                pass
            elif x > button2[0] and x < button2[2] and y > button2[1] and y < button2[3]:
                pass
            elif x > button3[0] and x < button3[2] and y > button3[1] and y < button3[3]:
                pass
            else:
                print("exec up")
                # record the ending (x, y) coordinates and indicate that
                # the cropping operation is finished
                ref_point.append((x, y))
                cropping = False
            
                # draw a rectangle around the region of interest
                #RGB_Decimal Value for Light Green color(0, 255, 0)
                cv2.rectangle(self.image, ref_point[0], ref_point[1], (0, 255, 0), 2)
                gen_buttons(self.image)
                # print("generated")
                cv2.imshow("image", self.image)    
        
        gen_buttons(self.image)
        print("called1")
        cv2.imshow("image", self.image)
        cv2.setMouseCallback("image", shape_selection)
        #cv2.setMouseCallback("image", btn_click_event)
  