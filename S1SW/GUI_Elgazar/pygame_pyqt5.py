import sys
import pygame
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QDesktopWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        pygame.init()

        self.label = QLabel("Start typing...", self)
        self.input_field = QLineEdit(self)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Connect the textChanged signal to a method
        self.input_field.textChanged.connect(self.update_label)

        # Set up a QTimer to periodically check Pygame events
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_pygame_events)
        self.timer.start(10)

    def update_label(self, text):
        self.label.setText(text)

    def check_pygame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
            elif event.type == pygame.KEYDOWN:
                print(f"Pygame key pressed: {pygame.key.name(event.key)}")

app = QApplication(sys.argv)

centerPoint = QDesktopWidget().availableGeometry().center()
window = MyWindow()
window.setGeometry(0, 0, 500, 100)
window.move(centerPoint)
window.setWindowTitle("Pygame/PyQt5")
window.show()

sys.exit(app.exec_())
