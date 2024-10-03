import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2 as cv

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.VBL = QVBoxLayout()
        
        self.feedLabel = QLabel()
        self.VBL.addWidget(self.feedLabel)
        
        self.cancelButton = QPushButton("Stop Webcam")
        self.cancelButton.clicked.connect(self.cancel)
        self.VBL.addWidget(self.cancelButton)
        
        self.worker = Worker()
        self.worker.img_update.connect(self.imgUpdate)
        self.worker.start()
        
        self.setLayout(self.VBL)
        
    def imgUpdate(self, img):
        self.feedLabel.setPixmap(QPixmap.fromImage(img))
        
    def cancel(self):
        self.worker.stop()  # Stop the worker thread
        QApplication.instance().quit()  # Close the application
        
    def closeEvent(self, event):
        self.worker.stop()  # Ensure the worker thread is stopped when closing
        event.accept()

class Worker(QThread):
    img_update = pyqtSignal(QImage)
    
    def run(self):
        self.thread_active = True
        cap = cv.VideoCapture(0)
        while self.thread_active:
            ret, frame = cap.read()
            if ret:
                img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                flipped_img = cv.flip(img, 1)
                convertToQformat = QImage(flipped_img.data, flipped_img.shape[1], flipped_img.shape[0], QImage.Format_RGB888)
                pic = convertToQformat.scaled(640, 480, Qt.KeepAspectRatio)
                self.img_update.emit(pic)
            QThread.msleep(30)  # Optional sleep to reduce CPU usage
        cap.release()  # Release the webcam
    
    def stop(self):
        self.thread_active = False
        self.quit()  # Stop the thread
        self.wait()  # Wait until the thread has fully stopped

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    root = MainWindow()
    root.show()
    
    sys.exit(app.exec_())
