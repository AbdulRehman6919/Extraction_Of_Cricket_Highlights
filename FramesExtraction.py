# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:19:17 2021

@author: Jan Family
"""
import cv2
from PyQt5.QtCore import *
from ProgressBar import ProgressBar
class FramesExtractor(QThread):
    change_value = pyqtSignal(int)
    def __init__(self,parent, cap,total,span,TotalVideoLength,FramePath,framespersecond):
        QThread.__init__(self, parent)
        self.init(cap,total,span,TotalVideoLength,FramePath,framespersecond)
    def init (self,cap,total,span,TotalVideoLength,FramePath,framespersecond):
        self.cap = cap
        self.total = total
        self.span = span
        self.TotalVideoLength = TotalVideoLength
        self.FramePath = FramePath
        self.framespersecond = framespersecond
    def run(self):
        self.record_frames_manual(self.cap,self.total,self.span,self.TotalVideoLength,self.FramePath,self.framespersecond)
        
    def record_frames_manual(self,cap,total,span,TotalVideoLength,FramePath,framespersecond):
        x=0
        pb = ProgressBar(self.TotalVideoLength)
        value=[0]
        seconds=1
        while True:
            grabbed, frame= self.cap.read()
            if not grabbed:
                break
            if self.total % self.span ==0:
       			
                if self.framespersecond != value[0]:
       				
                    filename = str(self.FramePath)+"/image" + "_"+str(int(seconds))+"."+str(int(x))+ ".png"
                    x=x+1
                else:
                    seconds=seconds+1
                    x=0
                    filename = str(self.FramePath)+"/image" +"_"+str(int(seconds))+"."+str(int(x)) + ".png"
                    x=x+1
                    value=[0]	
                value[0]=int(value[0])+int(self.span)
                frame=cv2.resize(frame,(1080,720))
                #progress(total,TotalVideoLength)
                pb=pb+self.span
                cv2.imwrite(filename, frame)
                
            self.total += 1
            self.change_value.emit(pb.prog)