# -*- coding: utf-8 -*-
"""
Created on Sun May  9 13:21:02 2021

@author: Abdul Rehman
"""
import cv2
from PyQt5.QtCore import *
from ProgressBar import ProgressBar
class TextRecognizer(QThread):
    change_value = pyqtSignal(int)
    Score_list_value=pyqtSignal(list)
    def __init__(self,parent,ref_point,FramePath,all_files):
        QThread.__init__(self, parent)
        self.init(ref_point,FramePath,all_files)
    def init (self,ref_point,FramePath,all_files):
        self.ref_point = ref_point
        self.all_files = all_files
        self.FramePath = FramePath
        

    def run(self):
        self.text_recog(self.ref_point,self.FramePath,self.all_files)
        
    def text_recog(self,ref_point,FramePath,all_files):

        import matplotlib.pyplot as plt
        from PIL import Image 
        import pytesseract  
        import tensorflow as tf
        import cv2
        import numpy as np
        import  PreProcessing as tm
        from ProgressBar import ProgressBar
        import os
        
        Scores_history=[]
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        config = ('-l eng --oem 3 --psm 10') 
        pb = ProgressBar(len(self.all_files))
        for i in self.all_files:
            new_img=cv2.imread(i)
            crop_img=new_img[self.ref_point[0][1]:self.ref_point[1][1], self.ref_point[0][0]:self.ref_point[1][0]] 
            grayImage = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
            #There is a need of transformation Law when images brighteness is faint, so we use it for now as comment
            Processed_Image=tm.PowerTransformation(grayImage)
            pb=pb+1
            if pb.prog<100:
                
                self.change_value.emit(pb.prog)
            else:
                self.change_value.emit(99)
                
            text=pytesseract.image_to_string(Processed_Image,config=config)
            Scores_history.append(text)      
            text=""
        self.Score_list_value.emit(Scores_history)
        
        print("\nScores Processes SuscessFully!")
        
    
    
    
    
    