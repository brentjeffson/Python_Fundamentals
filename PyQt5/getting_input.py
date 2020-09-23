import sys
from functools import partial
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit

def print_input(widget):
    print(widget.text())
    widget.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()

    win.setWindowTitle('Getting Input')

    txt_input = QLineEdit(win)
    txt_input.returnPressed.connect(partial(print_input, txt_input))

    win.show()
    sys.exit(app.exec_())

