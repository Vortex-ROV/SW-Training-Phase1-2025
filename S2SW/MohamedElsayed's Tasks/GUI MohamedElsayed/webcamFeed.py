import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 780, 500))
        self.label.setObjectName("label")

        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(350, 520, 100, 40))
        self.stop_button.setObjectName("stop_button")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Webcam Feed"))
        self.label.setText(_translate("MainWindow", "Waiting for webcam..."))
        self.stop_button.setText(_translate("MainWindow", "Stop Webcam"))

class WebcamThread(QThread):
    frame_signal = pyqtSignal(QImage)

    def run(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            ret, frame = self.cap.read()
            if ret:
                height = 500
                width = 780
                resized_frame = cv2.resize(frame, (width, height))
                rgb_image = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
                qt_image = QImage(rgb_image.data, width, height, QImage.Format_RGB888)
                self.frame_signal.emit(qt_image)

    def stop(self):
        self.cap.release()
        self.quit()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.webcam_thread = WebcamThread()
        self.webcam_thread.frame_signal.connect(self.update_image)
        self.webcam_thread.start()

        self.ui.stop_button.clicked.connect(self.stop_webcam)

    def update_image(self, qt_image):
        pixmap = QPixmap.fromImage(qt_image)
        self.ui.label.setPixmap(pixmap)

    def stop_webcam(self):
        self.webcam_thread.stop()
        self.ui.label.setText("Webcam stopped.")  # Update label text when webcam stops

    def closeEvent(self, event):
        self.webcam_thread.stop()
        event.accept()

app = QtWidgets.QApplication(sys.argv)
MainWindow = MainWindow()
MainWindow.show()
sys.exit(app.exec_())
