# main.py
from PyQt5 import QtWidgets
from front import Ui_Form  # Import your generated UI class
import sys
import re

class CalculatorApp(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ans = 0

        # Connect buttons to respective slots
        self.button_0.clicked.connect(lambda: self.button_pressed("0"))
        self.button_1.clicked.connect(lambda: self.button_pressed("1"))
        self.button_2.clicked.connect(lambda: self.button_pressed("2"))
        self.button_3.clicked.connect(lambda: self.button_pressed("3"))
        self.button_4.clicked.connect(lambda: self.button_pressed("4"))
        self.button_5.clicked.connect(lambda: self.button_pressed("5"))
        self.button_6.clicked.connect(lambda: self.button_pressed("6"))
        self.button_7.clicked.connect(lambda: self.button_pressed("7"))
        self.button_8.clicked.connect(lambda: self.button_pressed("8"))
        self.button_9.clicked.connect(lambda: self.button_pressed("9"))

        self.button_plus.clicked.connect(lambda: self.operator_pressed("+"))
        self.button_minus.clicked.connect(lambda: self.operator_pressed("-"))
        self.button_multiply.clicked.connect(lambda: self.operator_pressed("*"))
        self.button_divide.clicked.connect(lambda: self.operator_pressed("/"))

        self.button_equal.clicked.connect(self.calculate_result)
        self.pushButton_16.clicked.connect(self.clear)  # Clear button

    def button_pressed(self, number):
        """Handle number button press."""
        self.append(number)        

    def operator_pressed(self, operator):
        """Handle operator button press."""
        self.append(operator)

    def calculate_result(self):
        """Calculate the result of the expression in the line edit."""
        try:
            current_text = self.lineEdit.text()
            # Here we can evaluate the expression using eval safely
            # Optionally, consider using a dedicated math parser for more complex calculations.
            result = eval(current_text)
            self.lineEdit.setText(str(result))
            self.ans = result
        except Exception as e:
            self.lineEdit.setText("Error")

    def clear(self):
        """Clear the line edit."""
        self.lineEdit.setText("")
        self.ans = 0

    def append(self, character):
        """Append a character to the current text."""
        current_text = self.lineEdit.text()
        self.lineEdit.setText(current_text + character)

    def tokenize_by_operators(self, expression):
        """Tokenize the expression by operators."""
        # Define the regular expression pattern to match operators and parentheses
        pattern = r'(\b\w+\b|[+\-*/=()])'
        # Use re.findall to split the string based on the pattern
        tokens = re.findall(pattern, expression)
        return tokens

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
