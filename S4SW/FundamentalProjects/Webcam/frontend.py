# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create a vertical layout
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        self.layout.setSpacing(20)  # Add some spacing between label and buttons

        # Create the label
        self.label = QtWidgets.QLabel("", self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # Center the label text
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)  # Allow it to expand
        self.layout.addWidget(self.label)  # Add label to the layout

        # Create a horizontal layout for buttons
        self.button_layout = QtWidgets.QHBoxLayout()

        # Create the webcam button
        self.openWebcam = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\basem\\new_project\\Desktop\\test\\../../../Meta_Project/Icons/camera.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openWebcam.setIcon(icon)
        self.openWebcam.setIconSize(QtCore.QSize(60, 30))  # Adjusted icon size for a smaller button
        self.openWebcam.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)  # Fixed size policy
        self.openWebcam.setMinimumSize(100, 50)  # Minimum size for the button
        self.button_layout.addWidget(self.openWebcam)  # Add to button layout

        # Create the second button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\basem\\new_project\\Desktop\\test\\../../../Meta_Project/Center.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(60, 30))  # Adjusted icon size for a smaller button
        self.pushButton_2.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)  # Fixed size policy
        self.pushButton_2.setMinimumSize(100, 50)  # Minimum size for the button
        self.button_layout.addWidget(self.pushButton_2)  # Add to button layout

        # Center the button layout
        self.button_layout.setAlignment(QtCore.Qt.AlignCenter)  # Center the buttons
        self.layout.addLayout(self.button_layout)  # Add the button layout to the main layout

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
