from PyQt5.QtWidgets import QApplication, QWidget
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle('Basic Window')

    win.resize(200, 200)
    win.move(0, 0)
    win.show()

    sys.exit(app.exec_())