# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage
import cv2 as cv

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(310, 500, 171, 61))
        self.StopButton.setObjectName("StopButton")
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 780, 480))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.cam = Cam()
        self.cam.ImageUpdate.connect(self.update_image)

        
        self.StopButton.clicked.connect(self.Stop_cam)

        
        self.cam.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WebCam Feed"))
        self.StopButton.setText(_translate("MainWindow", "Stop webcam"))

    
    def update_image(self, Image):
    
        scaled_image = Image.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(QtGui.QPixmap.fromImage(scaled_image))

    
    def Stop_cam(self):
        self.cam.stop()

class Cam(QThread):
    # Define a signal to update the GUI with new frames
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        self.ThreadActive = True
        capture = cv.VideoCapture(0)  
        
        if not capture.isOpened():
            print("Error: Could not open webcam.")
            return
        capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
        capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

        while self.ThreadActive:
            ret, frame = capture.read()
            if ret:
                flipped_frame = cv.flip(frame, 1)
                Image = cv.cvtColor(flipped_frame, cv.COLOR_BGR2RGB)
                height, width, channel = Image.shape
                step = channel * width
                qImg = QImage(Image.data, width, height, step, QImage.Format_RGB888)
                self.ImageUpdate.emit(qImg)
                
        capture.release()

    def stop(self):
        # Stop the thread and immediately terminate the video feed
        self.ThreadActive = False
        self.quit()  
        self.wait()  # Wait for the thread to finish execution before exiting

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
