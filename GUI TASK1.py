import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout

class SimpleCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Calculator')
        self.setGeometry(200, 200, 300, 200)
        self.createUI()

    def createUI(self):
        vbox = QVBoxLayout()  #vertical widget
        self.display = QLineEdit(self)
        vbox.addWidget(self.display)   #display vertical widget
        gridLayout = QGridLayout()

        # buttons
        self.button_7 = QPushButton('7', self)
        self.button_8 = QPushButton('8', self)
        self.button_9 = QPushButton('9', self)
        self.button_div = QPushButton('/', self)
        self.button_4 = QPushButton('4', self)
        self.button_5 = QPushButton('5', self)
        self.button_6 = QPushButton('6', self)
        self.button_mul = QPushButton('*', self)
        self.button_1 = QPushButton('1', self)
        self.button_2 = QPushButton('2', self)
        self.button_3 = QPushButton('3', self)
        self.button_sub = QPushButton('-', self)
        self.button_0 = QPushButton('0', self)
        self.button_clear = QPushButton('C', self)
        self.button_equal = QPushButton('=', self)
        self.button_add = QPushButton('+', self)

        # (button text , row, col)
        buttons = [
            (self.button_7, 0, 0), (self.button_8, 0, 1), (self.button_9, 0, 2), (self.button_div, 0, 3),
            (self.button_4, 1, 0), (self.button_5, 1, 1), (self.button_6, 1, 2), (self.button_mul, 1, 3),
            (self.button_1, 2, 0), (self.button_2, 2, 1), (self.button_3, 2, 2), (self.button_sub, 2, 3),
            (self.button_0, 3, 0), (self.button_clear, 3, 1), (self.button_equal, 3, 2), (self.button_add, 3, 3)
        ]

        for button, row, col in buttons:
            gridLayout.addWidget(button, row, col)

        #connnect : to connect the button to its method
        self.button_7.clicked.connect(lambda: self.on_digit_click('7'))  # The lambda function allows us to pass the digit to the function.
        self.button_8.clicked.connect(lambda: self.on_digit_click('8'))
        self.button_9.clicked.connect(lambda: self.on_digit_click('9'))
        self.button_div.clicked.connect(lambda: self.on_operator_click('/'))
        self.button_4.clicked.connect(lambda: self.on_digit_click('4'))
        self.button_5.clicked.connect(lambda: self.on_digit_click('5'))
        self.button_6.clicked.connect(lambda: self.on_digit_click('6'))
        self.button_mul.clicked.connect(lambda: self.on_operator_click('*'))
        self.button_1.clicked.connect(lambda: self.on_digit_click('1'))
        self.button_2.clicked.connect(lambda: self.on_digit_click('2'))
        self.button_3.clicked.connect(lambda: self.on_digit_click('3'))
        self.button_sub.clicked.connect(lambda: self.on_operator_click('-'))
        self.button_0.clicked.connect(lambda: self.on_digit_click('0'))
        self.button_clear.clicked.connect(self.on_clear_click)
        self.button_equal.clicked.connect(self.on_equals_click)
        self.button_add.clicked.connect(lambda: self.on_operator_click('+'))



        vbox.addLayout(gridLayout)
        self.setLayout(vbox)


    def on_digit_click(self, digit):
        current_text = self.display.text()
        self.display.setText(current_text + digit)


    def on_operator_click(self, operator):
        current_text = self.display.text()
        self.display.setText(current_text + operator)


    def on_clear_click(self):
        self.display.clear()


    def on_equals_click(self):

            result = eval(self.display.text())  # fn exal ()
            self.display.setText(str(result))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = SimpleCalculator()
    calculator.show()
    sys.exit(app.exec_())
