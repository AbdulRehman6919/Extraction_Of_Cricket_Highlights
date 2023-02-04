# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\SplashScreen.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(556, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_bg_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_bg_frame.setGeometry(QtCore.QRect(20, 69, 450, 250))
        self.main_bg_frame.setStyleSheet("\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.926364, y2:0.79, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(23, 89, 159, 255));\n"
"border: 5px solid rgb(16, 62, 111) ; \n"
"border-radius: 20px;\n"
"")
        self.main_bg_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_bg_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_bg_frame.setObjectName("main_bg_frame")
        self.label = QtWidgets.QLabel(self.main_bg_frame)
        self.label.setGeometry(QtCore.QRect(90, 20, 400, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(217, 164, 17);\n"
"border:none;\n"
"background-color:none;")
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.main_bg_frame)
        self.progressBar.setGeometry(QtCore.QRect(10, 140, 381, 31))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"border-style:node;\n"
"border-radius: 10px;\n"
"color:rgb(255, 255, 255);\n"
"text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"border-style:node;\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(206, 0, 1, 255), stop:1 rgba(248, 67, 11, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.main_bg_frame)
        self.label_3.setGeometry(QtCore.QRect(160, 220, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(207, 207, 207);\n"
"background-color:none;\n"
"border-style:none;")
        self.label_3.setObjectName("label_3")
        self.cricket_border_frame = QtWidgets.QFrame(self.centralwidget)
        self.cricket_border_frame.setGeometry(QtCore.QRect(310, 29, 230, 251))
        self.cricket_border_frame.setStyleSheet("border: 0px")
        self.cricket_border_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cricket_border_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cricket_border_frame.setObjectName("cricket_border_frame")
        self.cricket_frame = QtWidgets.QFrame(self.centralwidget)
        self.cricket_frame.setGeometry(QtCore.QRect(290, 10, 300, 300))
        self.cricket_frame.setStyleSheet("image: url(:/images/cricket_1.png);border: 0px;border-style: none;")
        self.cricket_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cricket_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cricket_frame.setObjectName("cricket_frame")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 80, 81, 71))
        self.frame.setStyleSheet("image:url(:/images/cricket_2.png);border: 0px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 180, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.cricket_border_frame.raise_()
        self.main_bg_frame.raise_()
        self.frame.raise_()
        self.cricket_frame.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "QUICK CRICKET"))
        self.label_3.setText(_translate("MainWindow", "Developed by : Abdul Rehman & Adeel Asghar"))
        self.label_2.setText(_translate("MainWindow", "Initializing Quick Cricket..."))


import cricket_images


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
