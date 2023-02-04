    # -*- coding: utf-8 -*-
"""
Created on Sun May  9 04:41:25 2021

@author: Guiz
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QLabel,QWidget,QApplication,QProgressBar,QVBoxLayout,QDialog,QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore  import *
from  GeneticAlgorithm import Genetic_Algo
global path_video
path_video=''
class Genetic_Algo_ui(QMainWindow):
    
    def __init__(self,widget,FilePath,ref_point,FramesPath):
        self.bestChromosome=[]
        self.widget = widget
        self.FilePath = FilePath
        self.ref_point = ref_point
        self.FramesPath = FramesPath
        super(Genetic_Algo_ui,self).__init__()
        loadUi("./Ui_s/GeneticAlgoUi.ui",self)
        self.button_connections()
        
    def button_connections(self):
         #Generate Button
         self.btn_next.clicked.connect(self.btn_gen_ftn)
        
         #Back Button
         self.btn_back.clicked.connect(self.btn_back_ftn)
        
         #Home Button
         self.btn_home.clicked.connect(self.btn_home_ftn)
         
         #Show Button
         self.btn_show.clicked.connect(self.btn_show_ftn)
     
    def btn_show_ftn(self):
        from  Main_ui import Window
        wid=QWidget()
        global path_video 
        print('Path of Video From Genetic Class: ',path_video)
        self.obj=Window(wid,path_video)
        self.obj.show()
        self.obj.gen_high.setEnabled(False )
        
        
    def onComplete_FullVideo(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Highlight Video SucessFully Generated!")
        msg.setWindowTitle("Information")       
        msg.exec_()    
        
    def btn_gen_ftn(self):
        
        GA=Genetic_Algo()
        if self.interest_box.isChecked()==False and self.vareity_box.isChecked()==False:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Please Select At Least One Value")
            msg.setWindowTitle("Error")       
            msg.exec_()
          
            
        elif self.interest_box.isChecked()==True  and self.vareity_box.isChecked()==False:
            
            print ('Interest Value: 1 and Spread Value: 0' )
            self.bestChromosome=GA.Genetic_Algorithm(1,0)
            print(self.bestChromosome)
            self.thread = GenerateVideo(self,self.bestChromosome)
            self.thread.start()
           

            Count_Sixes=self.bestChromosome.count(6)
            Count_Fours=self.bestChromosome.count(4)
            Count_Outs=self.bestChromosome.count(0)
            Count_Events=self.bestChromosome.count(2)
            
            
            result_show="Summary:\n\tSixes: "+str(Count_Sixes)+"\n\tFours: "+str(Count_Fours)+"\n\tOuts: "+str(Count_Outs)+"\n\tEvents: "+str(Count_Events)
            self.result_label.setText(result_show)
            
            self.thread.finished.connect(self.onComplete_FullVideo)
             
        elif  self.interest_box.isChecked()==False  and self.vareity_box.isChecked()==True :
            print ('Interest Value: 0 and Spread Value: 1' )
            
            self.bestChromosome=GA.Genetic_Algorithm(0,1)
            print(self.bestChromosome)
            self.thread = GenerateVideo(self,self.bestChromosome)
            self.thread.start()
         
            
            Count_Sixes=self.bestChromosome.count(6)
            Count_Fours=self.bestChromosome.count(4)
            Count_Outs=self.bestChromosome.count(0)
            Count_Events=self.bestChromosome.count(2)
            
            result_show="Summary:\n\tSixes: "+str(Count_Sixes)+"\n\tFours: "+str(Count_Fours)+"\n\tOuts: "+str(Count_Outs)+"\n\tEvents: "+str(Count_Events)
            self.result_label.setText(result_show)
            
        
            self.thread.finished.connect(self.onComplete_FullVideo)
             
        elif self.interest_box.isChecked()==True and self.vareity_box.isChecked()==True:
            print ('Interest Value: 0.5 and Spread Value: 0.5' )
               
            self.bestChromosome=GA.Genetic_Algorithm(0.5,0.5)
            print(self.bestChromosome)
            self.thread = GenerateVideo(self,self.bestChromosome)
            self.thread.start()
     
            
            Count_Sixes=self.bestChromosome.count(6)
            Count_Fours=self.bestChromosome.count(4)
            Count_Outs=self.bestChromosome.count(0)
            Count_Events=self.bestChromosome.count(2)
            
            result_show="Summary:\n\tSixes: "+str(Count_Sixes)+"\n\tFours: "+str(Count_Fours)+"\n\tOuts: "+str(Count_Outs)+"\n\tEvents: "+str(Count_Events)
            self.result_label.setText(result_show)
                          
    
            self.thread.finished.connect(self.onComplete_FullVideo)

        
    def btn_back_ftn(self):
        from TextDetectionUi import TextDetectionWindow
        ui= TextDetectionWindow(self.widget,self.FramesPath,self.ref_point,self.FilePath)
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

class GenerateVideo(QThread):
     def __init__(self,parent,bestChromosome):
        QThread.__init__(self, parent)
        self.bestChromosome=bestChromosome
        
     def run(self):
        self.Gen_video(self.bestChromosome)
     def Gen_video(self,bestone):  
        import glob 
        import random as rd 
        import os 
        import shutil
        import subprocess as sb 
        
        Path_Four_files= glob.glob("./Runs/Fours"+"/*.mp4")
        Path_Six_files= glob.glob("./Runs/Sixes"+"/*.mp4")
        Path_Out_files= glob.glob("./Runs/Outs"+"/*.mp4")
        Path_Events_files= glob.glob("./Runs/Events"+"/*.mp4")
        
        
        
        new_list=[]  
        for i in bestone:
            if i ==6:
                while True:
                    temp=rd.choice(Path_Six_files)
                    if temp not in new_list:
                        new_list.append(temp)
                        break
                    else:
                        continue
            elif i ==4:
                while True:
                    temp=rd.choice(Path_Four_files)
                    if temp not in new_list:
                        new_list.append(temp)
                        break
                    else:
                        continue
            elif i ==0:
                while True:
                    temp=rd.choice(Path_Out_files)
                    if temp not in new_list:
                        new_list.append(temp)
                        break
                    else:
                        continue
            else:
                while True:
                    temp=rd.choice(Path_Events_files)
                    if temp not in new_list:
                        new_list.append(temp)
                        break
                    else:
                        continue
        print('Length of new_list  is : ',len(new_list))  
        new_list1=[]            
        for i in new_list:
            temp=i.split('\\')
            temp1=temp[1].split('_')
            new_list1.append([temp[0],int(temp1[0]),temp1[1]])
        
        new_list1.sort(key = lambda new_list1: new_list1[1]) 
          
        highlight_list=[]
        for i in new_list1:
            name=i[0]+str('\\')+str(i[1])+str('_')+str(i[2])
            highlight_list.append(name)
        
        '''for i in new_list1:
            highlight_list.append(i[2:])'''
        
        print(highlight_list)
        
        
        if os.path.isdir('./Save_Video_Clips'):
            shutil.rmtree('./Save_Video_Clips')
        os.mkdir('./Save_Video_Clips')    
    
        
        si = sb.STARTUPINFO()
        si.dwFlags |= sb.STARTF_USESHOWWINDOW
        
        Smooth_file=open('Smooth_file.txt','w')
        for i,j in enumerate( highlight_list):
         
            sb.call("ffmpeg -i "+j+" -s hd720 -r 30000/1001 -video_track_timescale 30k -c:a copy Save_Video_Clips/"+str(i)+".mp4", startupinfo=si)
            formats='file '+'Save_Video_Clips/'+str(i)+'.mp4'
            Smooth_file.write(formats)
            Smooth_file.write('\n')
            
        Smooth_file.close()
        
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        global path_video
        
        if os.path.isdir('./FinalVideo'):
            
            path_video="./FinalVideo/Highlighted_Video_"+str(current_time)+".mp4"
            sb.call("ffmpeg -f concat -safe 0 -i Smooth_file.txt -c copy  "+path_video, startupinfo=si)
            
        else:    
            os.mkdir('./FinalVideo')
            
            path_video="./FinalVideo/Highlighted_Video_"+str(current_time)+".mp4"
            sb.call("ffmpeg -f concat -safe 0 -i Smooth_file.txt -c copy  "+path_video, startupinfo=si)
        
