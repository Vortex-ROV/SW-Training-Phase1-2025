from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        
        self.setGeometry(200, 200, 250, 350)
        self.setWindowTitle('Calculator')
        self.initUI()
        
    def initUI(self):
        self.current_num = 0
        self.operator = None
        self.new_number_input = True  # Flag to check if we need to reset display
        
        self.label = QtWidgets.QPushButton(self)   
        self.label.setText('0')  # Initial display text
        self.label.setGeometry(10, 20, 230, 40) 
        
        # Define buttons
        self.b1 = QtWidgets.QPushButton('1',self)
        self.b2 = QtWidgets.QPushButton('2',self)
        self.b3 = QtWidgets.QPushButton('3',self)
        self.b4 = QtWidgets.QPushButton('4',self)
        self.b5 = QtWidgets.QPushButton('5',self)
        self.b6 = QtWidgets.QPushButton('6',self)
        self.b7 = QtWidgets.QPushButton('7',self)
        self.b8 = QtWidgets.QPushButton('8',self)
        self.b9 = QtWidgets.QPushButton('9',self)
        self.b0 = QtWidgets.QPushButton('0',self)
        self.c = QtWidgets.QPushButton('c',self)
        self.equal = QtWidgets.QPushButton('=',self)
        self.div = QtWidgets.QPushButton('/',self)
        self.pow = QtWidgets.QPushButton('*',self)
        self.minus = QtWidgets.QPushButton('-',self)
        self.add = QtWidgets.QPushButton('+',self)

        self.b1.setGeometry(10, 200, 50, 50)
        self.b2.setGeometry(70, 200, 50, 50)
        self.b3.setGeometry(130, 200, 50, 50)
        self.minus.setGeometry(190, 200, 50, 50)

        self.b4.setGeometry(10, 140, 50, 50)
        self.b5.setGeometry(70, 140, 50, 50)
        self.b6.setGeometry(130, 140, 50, 50)
        self.pow.setGeometry(190, 140, 50, 50)

        self.b7.setGeometry(10, 80, 50, 50)
        self.b8.setGeometry(70, 80, 50, 50)
        self.b9.setGeometry(130, 80, 50, 50)
        self.div.setGeometry(190, 80, 50, 50)

        self.b0.setGeometry(10, 260, 50, 50)
        self.c.setGeometry(70, 260, 50, 50)
        self.equal.setGeometry(130, 260, 50, 50)
        self.add.setGeometry(190, 260, 50, 50)

        # Connect buttons to functions
        self.b1.clicked.connect(lambda: self.clicked(self.b1))
        self.b2.clicked.connect(lambda: self.clicked(self.b2))
        self.b3.clicked.connect(lambda: self.clicked(self.b3))
        self.b4.clicked.connect(lambda: self.clicked(self.b4))
        self.b5.clicked.connect(lambda: self.clicked(self.b5))
        self.b6.clicked.connect(lambda: self.clicked(self.b6))
        self.b7.clicked.connect(lambda: self.clicked(self.b7))
        self.b8.clicked.connect(lambda: self.clicked(self.b8))
        self.b9.clicked.connect(lambda: self.clicked(self.b9))
        self.b0.clicked.connect(lambda: self.clicked(self.b0))

        self.add.clicked.connect(lambda: self.set_operator('+'))
        self.minus.clicked.connect(lambda: self.set_operator('-'))
        self.pow.clicked.connect(lambda: self.set_operator('*'))
        self.div.clicked.connect(lambda: self.set_operator('/'))
        self.equal.clicked.connect(self.result)
        self.c.clicked.connect(self.reset)

    def clicked(self, button):
        if self.new_number_input:  #if true (no new input yet)
            self.label.setText(button.text())  # Set current number
            self.new_number_input = False  
        else:
            # tens or hundreds 
            self.label.setText(self.label.text() + button.text())

    def set_operator(self, op):
        if not self.new_number_input:  # new.input-->false (due to a value presence in screen) Only store the number if it's not a new_num
            new_num = float(self.label.text())
            if self.operator:  # If there is already an operator, calculate
                self.calculate(new_num)  # Calculate with the previous operator
            else:
                self.current_num = new_num  # Set current number for the first time

            self.operator = op  
            self.new_number_input = True  # Prepare for new number input
            self.label.setText('0') 

    def calculate(self, new_num):
        if self.operator == '+':
            self.current_num += new_num
        elif self.operator == '-':
            self.current_num -= new_num
        elif self.operator == '*':
            self.current_num **= new_num
        elif self.operator == '/':
            if new_num != 0:
                self.current_num /= new_num
            else:
                self.label.setText("Error")  

    def result(self):
        if not self.new_number_input:  # the last number to be added or sub or...
            new_num = float(self.label.text())  
            self.calculate(new_num)  # Calculate with the last operator
            self.label.setText(str(self.current_num)) 
            self.operator = None  

    def reset(self):
        self.current_num = 0
        self.operator = None
        self.new_number_input = True
        self.label.setText('0')

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
