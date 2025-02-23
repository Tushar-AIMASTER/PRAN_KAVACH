

### Project Title: PRAN KAVACH
### Project Description: This project is a Drowsiness Detection System which will detect the drowsiness of the driver and will alert the driver to take a break. This project will also keep the record of the drowsiness detected by the system.
#### Team Name: ANARGHYA
#### Team Members:
#### Name: Tushar Srivastava
#### Name: Arpit Raj Katiyar
#### Name: Satvik Yadav
#### Name: Mayank Kumar Kashyap
# Installing the libraries needed for the Detector:

# Importing the Libraries:

import scipy
from scipy.spatial import distance as dist
from imutils import face_utils
import imutils
import dlib
import cv2
import winsound
import time
import pyttsx3
import datetime
import speech_recognition as sr
import os
import sys
import pyautogui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import datetime as dt
from datetime import date as d
import glob
import os.path
import webbrowser
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)

# Initializing Beep Sound

frequency = 2500
duration = 1000 # here 1000 resemble 1 second

# Initializing Speak

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Buliding GUI & MAIN PROGRAM

# Creating G.U.I. with PyQt5

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1207, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Live_preview = QtWidgets.QLabel(self.centralwidget)
        self.Live_preview.setGeometry(QtCore.QRect(60, 140, 561, 511))
        self.Live_preview.setStyleSheet("border: 2px solid black;\n"
"border-radius: 7px;")
        self.Live_preview.setFrameShape(QtWidgets.QFrame.Box)
        self.Live_preview.setText("")
        self.Live_preview.setObjectName("Live_preview")
        self.NAVBAR = QtWidgets.QFrame(self.centralwidget)
        self.NAVBAR.setGeometry(QtCore.QRect(0, 0, 1201, 91))
        self.NAVBAR.setStyleSheet("border: 1px solid black;")
        self.NAVBAR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NAVBAR.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NAVBAR.setObjectName("NAVBAR")
        self.label = QtWidgets.QLabel(self.NAVBAR)
        self.label.setGeometry(QtCore.QRect(490, 10, 251, 71))
        self.label.setStyleSheet("border: 0px;\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.status = QtWidgets.QTextEdit(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(870, 144, 104, 31))
        self.status.setObjectName("status")
        self.live_indicator = QtWidgets.QTextEdit(self.centralwidget)
        self.live_indicator.setGeometry(QtCore.QRect(70, 150, 81, 31))
        self.live_indicator.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(0,0,0,0.1);")
        self.live_indicator.setObjectName("live_indicator")
        self.alert = QtWidgets.QTextEdit(self.centralwidget)
        self.alert.setGeometry(QtCore.QRect(740, 180, 371, 411))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.alert.setStyleSheet("border: 2px solid black;\n"
"border-radius: 7px;")
        self.alert.setObjectName("alert")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1211, 861))
        self.widget.setStyleSheet("border: 1px solid black;\n"
"border-radius: 7px;\n"
"font-size: 14px;\n"
"font-family: Impact;\n"

"\n"
"")
        self.widget.setStyleSheet("background: beige;\n"
"")
        self.widget.setObjectName("widget")
        self.History = QtWidgets.QPushButton(self.widget)
        self.History.setEnabled(True)
        self.History.setGeometry(QtCore.QRect(230, 700, 131, 61))
        self.History.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.History.setFont(font)
        self.History.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.History.setStyleSheet("border: 1px solid black;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.History.setObjectName("History")
        self.start = QtWidgets.QPushButton(self.widget)
        self.start.setGeometry(QtCore.QRect(70, 700, 121, 61))
        self.start.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.start.setFont(font)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start.setMouseTracking(False)
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet("border: 1px solid black;\n"
"border-radius: 7px\n"
"")
        self.start.setAutoRepeat(True)
        self.start.setAutoRepeatDelay(20)
        self.start.setAutoRepeatInterval(20)
        self.start.setAutoDefault(False)
        self.start.setObjectName("start")
        self.History_2 = QtWidgets.QPushButton(self.widget)
        self.History_2.setEnabled(True)
        self.History_2.setGeometry(QtCore.QRect(980, 690, 131, 61))
        self.History_2.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.History_2.setFont(font)
        self.History_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.History_2.setStyleSheet("border: 1px solid black;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.History_2.setObjectName("History_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 790, 1211, 87))
        self.plainTextEdit.setStyleSheet("background-color: rgb(96, 255, 255);\n"
"color: black;\n"
"\n"
" background-color: #2E2E2E;\n"
"    color: #FFFFFF;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"    border-top: 1px solid #444444;\n"
"   qproperty-alignment: \'AlignCenter\';")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.widget.raise_()
        self.alert.raise_()
        self.NAVBAR.raise_()
        self.Live_preview.raise_()
        self.status.raise_()
        self.live_indicator.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.start.clicked.connect(self.detectionFunction)

        self.History.clicked.connect(self.historyFunction)
        
        self.History_2.clicked.connect(self.aboutFunction)
        
    def __init__(self):
        super().__init__()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.status.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">STATUS</span></p></body></html>"))
        self.live_indicator.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">LIVE</span></p></body></html>"))
        self.History.setText(_translate("MainWindow", "HISTORY"))
        self.start.setText(_translate("MainWindow", "START"))
        self.History_2.setText(_translate("MainWindow", "ABOUT US"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "                                                                                                               © 2025 ANARGHYA                 All Rights Reserved"))

    def detectionFunction(self):
        self.alert.setText("Initializing...") # This will put text in status bar of GUI
        # This will get current working directory:
        path = os.getcwd()
        os.chdir(path)
        # Creating the function to get the eye aspect ratio:
        def eyeAspectRatio(eye):
            A = dist.euclidean(eye[1], eye[5])
            B = dist.euclidean(eye[2], eye[4])
            C = dist.euclidean(eye[0], eye[3])
            # Here ear mean eye aspect ratio
            ear = (A + B) / (2.0 * C)# This will give us the average & because we have two eyes therefore dividing by 2
            return ear


        # Creating a function to make the detector give reminder for breaks every 3 hours:
        def currentTime():
            return datetime.datetime.strftime(datetime.datetime.today() , '%d/%m/%Y-%Hh/%Mm')
              
        three_Hour_Later = datetime.datetime.today() + datetime.timedelta(minutes=3)
        three_h=datetime.datetime.strftime(three_Hour_Later , '%d/%m/%Y-%Hh/%Mm')
        # This functiion will make the detector speak & print to take a break:
        def remind():
            text = "Please take a break, you have been driving the vehicle continously for {0} hours".format(3)
            print(text)
            speak(text)

        # Initializing some values to some variable
        count = 0
        earThresh = 0.3 # Distance between vertical eye coordinate Threshold
        earFrames = 45 # Consecutive frames for eye closure
        # Locating the predicitor file and assigning the variable
        shapePredictor = "shape_predictor_68_face_landmarks.dat"
        # This command will connect the camera for taking the input:
        cam = cv2.VideoCapture(0)
        # Loading the detector for the program:
        detector = dlib.get_frontal_face_detector()
        # Passing the algorithm file into the predicitor:
        predictor = dlib.shape_predictor(shapePredictor)

        # Getting  the coordinates of the  left & right eye
        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
        while True:
            # Reading the feed from the camera :
            _, frame = cam.read()
            # Resizing the images obtaining from the camera:
            frame = imutils.resize(frame, width=561,height=511)
            # converting the images into grayscale image for further processing:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rects = detector(gray, 0)
            '''cv2.putText(frame, "press 'q' to exit", (270, 320),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 100, 255), 2)'''


            for rect in rects:
                shape = predictor(gray, rect)
                # here we are converting the points location in an array:
                shape = face_utils.shape_to_np(shape)

                leftEye = shape[lStart:lEnd]
                rightEye = shape[rStart:rEnd]
                leftEAR = eyeAspectRatio(leftEye)
                rightEAR = eyeAspectRatio(rightEye)

                ear = (leftEAR + rightEAR) / 2.0

                leftEyeHull = cv2.convexHull(leftEye)
                rightEyeHull = cv2.convexHull(rightEye)
                cv2.drawContours(frame, [leftEyeHull], -1, (0, 0, 255), 1)
                cv2.drawContours(frame, [rightEyeHull], -1, (0, 0, 255), 1)
                self.alert.setText("Detecting...")

                # this will compare the current ear value with the predefined
                if ear < earThresh:
                    count += 1

                    if count >= earFrames:
                        cv2.putText(frame, "DROWSINESS DETECTED", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        winsound.Beep(frequency, duration) # This will create a beep sound
                        pyautogui.press("volumeup",presses=5) # This will increase the volume & intensity of sound
                        now = dt.now() # This get the time when drowisness was detected
                        current_time = now.strftime("%H:%M:%S")
                        today = d.today() # This get the current date
                        d2 = today.strftime("%B %d, %Y")
                        # This will check if text file exists or not , if exist then append new entries and if not exist then will create a new file to save info.
                        
                        if os.path.exists('History.txt')==True:
                            f = open("History.txt", "a")
                            f.write("\n  Drowisness Detected on "+d2+" at "+current_time+"\n")
                            f.close()
                        else:
                            with open('History.txt', 'w') as f:
                                f.write("\n  Drowisness Detected on "+d2+" at ",current_time+"\n")
                        print("Drowisness Detected on "+ d2+" at "+ current_time)
                        self.alert.setText("Drowisness Detected")

                else:
                    count = 0
                    self.alert.setText("Detecting...")
            # This will dispaly the Detector's output interface:
            #cv2.imshow("DETECTOR", frame)


            image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_BGR888)
            self.Live_preview.setPixmap(QtGui.QPixmap.fromImage(image))
            # This will take the keyboard input:
            key = cv2.waitKey(1) & 0xFF
            # To Close the pop up window which appear press "q" on the keyboard:
            if key == ord("q") or key == ord("Q"):# This line will take the input from the keyboard in the background & if it is "q" then the program will terminate.
                break
            # This will compare the current time with the re,=minder time :
            if currentTime()==three_h: # when the both with will equall then it will give the reminder.
                remind()



        #These command will release the camera and close the window:
        cam.release()
        cv2.destroyAllWindows()
    def historyFunction(self):
        webbrowser.open("HISTORY.txt") # This will open the text file when History button is clicked on the GUI
    def aboutFunction(self):
        webbrowser.open("https://pran-kavach.netlify.app/") # This will open the about us page when About us button is clicked on the GUI



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    