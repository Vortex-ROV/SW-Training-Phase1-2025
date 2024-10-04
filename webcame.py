import cv2
import sys
from PyQt5 import QtWidgets ,QtGui,QtCore

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('webcame')
        self.setGeometry(100,100,400,400)
        
        self.image =QtWidgets.QLabel(self)
        self.image.setGeometry(10,10,380,330)
        
        self.start = QtWidgets.QPushButton('start webcame',self)
        self.start.setGeometry(10,360,100,30)
        self.start.clicked.connect(self.start_web)
        
        self.end = QtWidgets.QPushButton('end webcame',self)
        self.end.setGeometry(120,360,100,30)
        self.end.clicked.connect(self.end_web)
        
        self.timer=QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)   
        
        
        
        
    def start_web(self):
        self.capture= cv2.VideoCapture(0)
        self.timer.start(20)
    def end_web(self):
        self.timer.stop()#
        if self.capture is not None:
            self.capture.release()
            self.capture = None
        self.image.clear() 
    def update_frame(self):
            if self.capture is not None:
                   ret, frame = self.capture.read()
                   if ret:
                        # Convert the frame from BGR to RGB format
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        # Convert to QImage format
                        height, width, channel = frame.shape
                        bytes_per_line = 3 * width
                        q_image = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
                        self.image.setPixmap(QtGui.QPixmap.fromImage(q_image))
    def closeEvent(self, event):
        self.stop_webcam()  # Stop webcam when closing the application
        event.accept()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()