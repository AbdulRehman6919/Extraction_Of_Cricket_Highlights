# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 18:15:37 2021

@author: Guiz
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QColor, qGray, QImage, QPainter, QPalette,QIcon
from PyQt5.QtCore import Qt, QUrl,QTime
import os



class Window(QWidget):
    def __init__(self,widget,filename):
        super().__init__()
        self.widget = widget
        self.filename = filename
        self.setWindowTitle("Quick Cricket")
        self.setGeometry(350, 100, 1000, 500)
        self.setWindowIcon(QIcon('./Images/cricket.png'))
        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)
        self.duration=0
        self.init_ui()
        self.check_file_available()
  

    def init_ui(self):

        #create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)

        #create videowidget object

        videowidget = QVideoWidget()


        #create open button
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)
        
        #create Generate Highlights button
        self.gen_high = QPushButton('Generate Highlights')
        self.gen_high.setObjectName("gen_high")
        self.gen_high.clicked.connect(self.gen_highlights_ftn)


        #create button for playing
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)



        #create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)



        #create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        #For Viewing Video Duration
        self.labelDuration = QLabel()
        
        #create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)

        #set widgets to the hbox layout
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)
        hboxLayout.addWidget(self.labelDuration)
        hboxLayout.addWidget(self.gen_high)
        



        #create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)


        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(videowidget)


        #media player signals

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def check_file_available(self):
        if self.filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
            self.playBtn.setEnabled(True)
            print('Path of Video From Main Ui Class: ',self.filename)
            if "Highlighted_Video" in self.filename :
                self.play_video()
        
            
    def open_file(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        self.check_file_available()
        
        
            

    def gen_highlights_ftn(self):
        
        if self.filename == '':
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Video not selected.\nSelect a cricket video.")
                msg.setWindowTitle("Error")
                msg.exec_()
        else:
            import SetSpanUi
            ui= SetSpanUi.SetSpanWindow(self.widget,self.filename)  
            self.widget.addWidget(ui)
            self.widget.setFixedHeight(375)
            self.widget.setFixedWidth(872)
            self.widget.setCurrentIndex(self.widget.currentIndex()+1)
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
        
            self.mediaPlayer.play()
    def durationChanged(self, duration):
            
            duration /= 1000
     
            self.duration = duration
            self.slider.setMaximum(duration)
        
    def positionChanged(self, progress):
            progress /= 1000
     
            if not self.slider.isSliderDown():
                self.slider.setValue(progress)
     
            self.updateDurationInfo(progress)
    def updateDurationInfo(self, currentInfo):
        duration = self.duration
        if currentInfo or duration:
            currentTime = QTime((currentInfo/3600)%60, (currentInfo/60)%60,
                    currentInfo%60, (currentInfo*1000)%1000)
            totalTime = QTime((duration/3600)%60, (duration/60)%60,
                    duration%60, (duration*1000)%1000);
 
            format = 'hh:mm:ss' if duration > 3600 else 'mm:ss'
            tStr = currentTime.toString(format) + " / " + totalTime.toString(format)
        else:
            tStr = ""
 
        self.labelDuration.setText(tStr)

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)

            )

        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)

            )

    def position_changed(self, position):
        self.slider.setValue(position)


    def duration_changed(self, duration):
        self.slider.setRange(0, duration)


    def set_position(self, position):
        self.mediaPlayer.setPosition(position)


    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())


#%%
'''

if __name__ == '__main__':
 
    import sys
    
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
    
    app = QApplication(sys.argv)
    app.setApplicationName("Quick Crciket")
    app.setWindowIcon(QIcon('./cricket.png'))
    app.setStyle("Fusion")
    
    
    

    #app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    app.setPalette(palette)
    widget= QtWidgets.QStackedWidget()
    window = Window(widget,'')
    widget.addWidget(window)
    widget.setFixedHeight(500)
    widget.setFixedWidth(1000)
    widget.show()
    sys.exit(app.exec_())


import os

filename='./Runs/Events\245_270.mp4'
print(filename)
Video_name=filename.split('Events')[1]
print(Video_name)
'''
#%%

'''
import glob 
Path_Four_files= glob.glob(".\\Runs\\Fours"+"\\*.mp4")
Path_Six_files= glob.glob(".\\Runs\\Sixes"+"\\*.mp4")
Path_Out_files= glob.glob(".\\Runs\\Outs"+"\\*.mp4")
Path_Events_files= glob.glob(".\\Runs\\Events"+"\\*.mp4")

print(Path_Four_files[0].split('\\'))

#%%

import glob 
import natsort as nt
        
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
    curr_file=curr_file[0]
    for j in range(i+1,len(All_Filenames)):
        next_file=All_Filenames[j].split('\\')
        next_file=next_file[3].split('_')
        next_file=next_file[0]
        if int(curr_file)> int(next_file):
            
                    #The above if else is used is curr_num is greater than next_num then it show be checked in that way
            if (int(curr_file)-int(next_file))<10 and All_Filenames[i] not in Delete_items:
                
                Delete_items.append(All_Filenames[i])
                Delete_items.append(All_Filenames[j])
                print('File i: ',All_Filenames[i],' File j: ',All_Filenames[j])
                        
        else:
                    
            if (int(next_file)-int(curr_file))<10 and All_Filenames[i] not in Delete_items:
                
                Delete_items.append(All_Filenames[i])
                Delete_items.append(All_Filenames[j])
                print('File i: ',All_Filenames[i],' File j: ',All_Filenames[j])
import os             
for (i,j) in zip(Delete_items,range(len(Delete_items))):
    if 'Events' in i:
                
        os.remove(i)
        Delete_items.pop(j)
                
print(Delete_items)               

        
'''