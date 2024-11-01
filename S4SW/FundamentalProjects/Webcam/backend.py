import cv2
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication
from webcam import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.cap = cv2.VideoCapture(0)
        
        # Setup the timer for continuous frame capture
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.start_cam(self.window.label))
        
        # Connect buttons
        self.window.openWebcam.clicked.connect(self.start_capture)
        self.window.pushButton_2.clicked.connect(self.stop_capture)
    
    def start_capture(self):
        self.timer.start(30)  # Capture frame every 30 ms

    def start_cam(self, label):
        ret, frame = self.cap.read()
        if ret:
            # Flip the image horizontally (use 0 for vertical flip)
            inverted_frame = cv2.flip(frame, 1)
        
            # Resize the frame for display
            resized_frame = cv2.resize(inverted_frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        
            # Convert to QImage and display
            image = QtGui.QImage(resized_frame, resized_frame.shape[1], resized_frame.shape[0], resized_frame.strides[0], QtGui.QImage.Format_BGR888)
            label.setPixmap(QtGui.QPixmap.fromImage(image))
    
    def stop_capture(self):
        self.timer.stop()
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
