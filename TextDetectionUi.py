# -*- coding: utf-8 -*-

"""
Created on Fri Apr 30 19:46:32 2021
@author: Guiz
"""



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QLabel,QWidget,QApplication,QProgressBar,QVBoxLayout,QDialog,QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore  import *
from TextRecognition import TextRecognizer
from AudioClipExtraction import AudioClipExtractor
import time

class TextDetectionWindow(QMainWindow):
    
    def __init__(self,widget,FramesPath,ref_point,FilePath):
        self.FilePath = FilePath
        self.ref_point = ref_point
        self.file = str('./Frames')
        self.widget = widget
        self.FramesPath = FramesPath
        super(TextDetectionWindow,self).__init__()
        loadUi("./Ui_s/TextDetectionUi.ui",self)
        self.Scores_history=[]
        self.button_connections()
        
    def button_connections(self):
        #Next Button
        self.btn_next.setEnabled(True)
        self.btn_next.clicked.connect(lambda: self.btn_next_ftn())
        
        #Back Button
        self.btn_back.clicked.connect(lambda: self.btn_back_ftn())
        
        #Proceed Button
        self.btn_proceed.clicked.connect(lambda: self.btn_proceed_ftn())
        
        #Home Button
        self.btn_home.clicked.connect(lambda: self.btn_home_ftn())
    
    
    def btn_next_ftn(self):
        from Genetic_Algo_Ui import Genetic_Algo_ui
        gen_algo_win = Genetic_Algo_ui(self.widget,self.FilePath,self.ref_point,self.FramesPath)
        self.widget.addWidget(gen_algo_win)
        self.widget.setFixedHeight(300)
        self.widget.setFixedWidth(500)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

  
    def btn_back_ftn(self):
        from SelectImageUi import SelectImageWindow
        select_img_win = SelectImageWindow(self.widget,self.FramesPath,self.FilePath)
        self.widget.addWidget(select_img_win)
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
        
    def updateProgressBar(self,val):
        self.progBar.setValue(val)
    def Scorelistval(self,val):
        self.Scores_history=val
    def sort_seq(self):
        #Reading All Images in Sequenece Wise


        import glob 
        import natsort as nt
        
        path = self.FramesPath # use your path
        all_files = glob.glob(path + "/*.png")
        self.all_files=nt.natsorted(all_files)
        print("sorted")
    
    def make_dirs(self):
        #Making Directories

        import os
        path = './Runs'
            
        self.SubPath_4=path+'/Fours'
        self.SubPath_6=path+'/Sixes' 
        self.SubPath_Out=path+'/Outs' 
        self.SubPath_Events=path+'/Events' 
        
        try:  
            
            if os.path.exists(path):
                    import shutil
                    shutil.rmtree(path)
            else:
                pass
            
            os.makedirs(path,exist_ok=True)        
            os.makedirs(self.SubPath_4,exist_ok=True)
            os.makedirs(self.SubPath_6,exist_ok=True)
            os.makedirs(self.SubPath_Out,exist_ok=True)
            os.makedirs(self.SubPath_Events,exist_ok=True)
    
        except OSError as error:  
            print("Unable to create a drirectory Directory Already Exixts!")
    def Crop_Video(self,start_time, end_time, targetname):
        orignal_path= self.FilePath
        from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
        ffmpeg_extract_subclip(orignal_path, start_time, end_time, targetname)
    
    def classify_events(self):
        import cv2 
        import os
        Fisrt_iteration=True  
        folder_counter_4=1 
        folder_counter_Out=1
        counting_that_place=0
        
        for i,j in zip(self.Scores_history,range(1,len(self.all_files)+1)):
            if '-' in i:  
                i=i.strip()
                temp=i.split('-')      
                if temp[0].isdigit() and temp[1].isdigit() :
            
                    if Fisrt_iteration == True:
                        Score_prev=int(temp[0])
                        Score_index_prev=j-1
                        Out_prev=int(temp[1])
                        Out_index_prev=j-1
                        Fisrt_iteration=False
                        continue              
                    else:
                        Score_curr=int(temp[0])
                        Out_curr=int(temp[1])
                        
                        if (Score_curr-Score_prev)==4:
                            
                  
                            #Splitting the filname and getting the seconds info from it 
                            second=self.all_files[j].split('_')
                            second=second[1].split('.')
                            seconds=second[0]
                            start_time=int(seconds)-15
                            end_time=int(seconds)+15
                    
                            
                            path4_subfolder=self.SubPath_4+"/"+str(start_time)+str("_")+str(end_time)+".mp4"
                            
                            self.Crop_Video(start_time,end_time,path4_subfolder )
                            
                            try:  
                                os.makedirs(path4_subfolder,exist_ok=True)
                            except OSError as error:  
                                print("Unable to create a folder_4 ")   
                                
                                
                                
                            Score_prev=Score_curr
                            Out_prev=Out_curr
                            Score_index_prev=j-1
                            Out_index_prev=j-1
                         
                        elif (Score_curr-Score_prev)==6:
                            
                            
                        
                            #Splitting the filname and getting the seconds info from it 
                            second=self.all_files[j].split('_')
                            second=second[1].split('.')
                            seconds=second[0]
                            start_time=int(seconds)-15
                            end_time=int(seconds)+15
                            
                            
                            path6_subfolder=self.SubPath_6+"/"+str(start_time)+str("_")+str(end_time)+".mp4"
                            
                            self.Crop_Video(start_time,end_time,path6_subfolder )
                            
                            try:  
                                os.makedirs(path6_subfolder,exist_ok=True)
                            except OSError as error:  
                                print("Unable to create a folder_6 ")   
                                
                            Score_prev=Score_curr
                            Out_prev=Out_curr
                            Score_index_prev=j-1
                            Out_index_prev=j-1   
                            
                        elif (Out_curr-Out_prev)==1:
                            
                            #Splitting the filname and getting the seconds info from it 
                            second=self.all_files[j].split('_')
                            second=second[1].split('.')
                            seconds=second[0]
                            start_time=int(seconds)-15
                            end_time=int(seconds)+15
                            
                        
                            pathOUT_subfolder=self.SubPath_Out+"/"+str(start_time)+str("_")+str(end_time)+".mp4"
                            self.Crop_Video(start_time,end_time,pathOUT_subfolder )
                            try:  
                                os.makedirs(pathOUT_subfolder,exist_ok=True)
                            except OSError as error:  
                                print("Unable to create a folder_OUT ")   
                                
        
                               
                            Score_prev=Score_curr
                            Out_prev=Out_curr
                            Score_index_prev=j-1
                            Out_index_prev=j-1
                            
                            
                        else:
                            Score_prev=Score_curr
                            Out_prev=Out_curr
                            Score_index_prev=j-1
                            Out_index_prev=j-1
    def audio_events(self):
        self.thread1 = AudioClipExtractor(self)
        self.thread1.start()
        self.thread1.finished.connect(self.onComplete_AudioClips)
    def DeleteRedundantEvents(self):
        import glob 
        import natsort as nt
        import os 
        
        Path_Four_files= glob.glob(".\\Runs\\Fours"+"\\*.mp4")
        Path_Six_files= glob.glob(".\\Runs\\Sixes"+"\\*.mp4")
        Path_Out_files= glob.glob(".\\Runs\\Outs"+"\\*.mp4")
        Path_Events_files= glob.glob(".\\Runs\\Events"+"\\*.mp4")
        
        All_Filenames=[]
        
        for i in Path_Four_files:
            All_Filenames.append(i)
        for i in Path_Six_files:
            All_Filenames.append(i)
        for i in Path_Out_files:
            All_Filenames.append(i)
        for i in Path_Events_files:
            All_Filenames.append(i)
        
        Delete_items=[]
        for i in range(len(All_Filenames)):
            curr_file=All_Filenames[i].split('\\')
            curr_file=curr_file[3].split('_')
            curr_file=curr_file[1].split('.')
            curr_file=curr_file[0]
            for j in range(i+1,len(All_Filenames)):
                next_file=All_Filenames[j].split('\\')
                next_file=next_file[3].split('_')
                next_file=next_file[0]
                if int(curr_file)> int(next_file):
                    #The above if else is used is curr_num is greater than next_num then it show be checked in that way
                    if (int(curr_file)-int(next_file))<=10 and All_Filenames[i] not in Delete_items:
                        Delete_items.append(All_Filenames[i])
                        Delete_items.append(All_Filenames[j])
                        print('File i: ',All_Filenames[i],' File j: ',All_Filenames[j])
                        
                else:
                    
                    if (int(next_file)-int(curr_file))<=10 and All_Filenames[i] not in Delete_items:
                        Delete_items.append(All_Filenames[i])
                        Delete_items.append(All_Filenames[j])
                        print('File i: ',All_Filenames[i],' File j: ',All_Filenames[j])
        
        Delete_item=[]    
        for i in Delete_items:
            if i not in Delete_item:
                Delete_item.append(i)
                
        for (i,j) in zip(Delete_item,range(len(Delete_item))):
            if 'Events' in i:
                
                os.remove(i)
                Delete_item.pop(j)
                
        print(Delete_item)
    
        
    def onComplete_AudioClips(self):
        
        self.DeleteRedundantEvents()
        self.prog_label.setText("Wait For Audio Completition Part...")
        
        self.updateProgressBar(100)
        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("All Clips Extracted SuccessFully")
        msg.setWindowTitle("Information")
        msg.exec_()   
        self.prog_label.setText("Completed Successfully!")  
        
        
    def onComplete(self):
        #Exceute te Remaining Part When Thread Completes
        self.prog_label.setText("Making Directories for Events......")
        self.make_dirs()
        time.sleep(2)
        self.prog_label.setText("Storing Events in the directories......")
        self.classify_events()
        self.audio_events()
                           
              
    def btn_proceed_ftn(self):
        self.prog_label.setText("Sorting extracted frames in sequence........")
        self.sort_seq()
        time.sleep(1)
        self.prog_label.setText("Detecting Scoreboard text & recognizing text......")

        self.thread = TextRecognizer(self,self.ref_point,self.FramesPath,self.all_files)
        self.thread.start()
        self.thread.change_value.connect(self.updateProgressBar)
        self.thread.Score_list_value.connect(self.Scorelistval)
        self.thread.finished.connect(self.onComplete)
        
        
        
       
        

        
        
        
        
        