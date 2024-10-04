import sys
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer


class PygameIntegration(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_pygame)
        self.timer.start(16)
        self.key_status = {
            pygame.K_UP: "Up: Released",
            pygame.K_DOWN: "Down: Released",
            pygame.K_LEFT: "Left: Released",
            pygame.K_RIGHT: "Right: Released",
        }

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label = QLabel("Press arrow keys to interact with PyQt5 UI", self)
        self.up_label = QLabel("Up: Released", self)
        self.down_label = QLabel("Down: Released", self)
        self.left_label = QLabel("Left: Released", self)
        self.right_label = QLabel("Right: Released", self)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.up_label)
        self.layout.addWidget(self.down_label)
        self.layout.addWidget(self.left_label)
        self.layout.addWidget(self.right_label)

        self.setLayout(self.layout)
        self.setWindowTitle("PyQt5 & Pygame Integration")
        self.show()

    def update_labels(self):
        self.up_label.setText(self.key_status[pygame.K_UP])
        self.down_label.setText(self.key_status[pygame.K_DOWN])
        self.left_label.setText(self.key_status[pygame.K_LEFT])
        self.right_label.setText(self.key_status[pygame.K_RIGHT])

    def update_pygame(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                self.close()

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key in self.key_status:
                    if event.type == pygame.KEYDOWN:
                        self.key_status[event.key] = (
                            f"{pygame.key.name(event.key).capitalize()}: Pressed"
                        )
                    elif event.type == pygame.KEYUP:
                        self.key_status[event.key] = (
                            f"{pygame.key.name(event.key).capitalize()}: Released"
                        )
        self.update_labels()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PygameIntegration()
    sys.exit(app.exec_())
