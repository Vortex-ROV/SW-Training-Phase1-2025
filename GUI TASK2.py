import sys
import cv2
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap

class WebcamApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("camera")
        self.setGeometry(200, 200, 300, 300)
        self.video_label = QLabel(self)
        self.video_label.setFixedSize(600, 400)

        layout = QVBoxLayout()
        layout.addWidget(self.video_label)

        frame = QWidget()
        frame.setLayout(layout)
        self.setCentralWidget(frame)

        self.is_running = True

        # Start thread
        self.video_thread = threading.Thread(target=self.update_video)
        self.video_thread.start()

    def update_video(self):
        cap = cv2.VideoCapture(0)

        while self.is_running:
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channel = frame.shape
                bytes_per_line = 3 * width
                q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)  #888 each color 1 byte
                self.video_label.setPixmap(QPixmap.fromImage(q_img))


        cap.release()

    def closeEvent(self, event):
        self.is_running = False
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebcamApp()
    window.show()
    sys.exit(app.exec_())
