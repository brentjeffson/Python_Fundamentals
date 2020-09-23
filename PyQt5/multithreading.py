from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QLabel
# from PyQt5.QtGui import
from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSlot
import time

class ExWorker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(ExWorker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        # print(self.args, self.kwargs)
        self.fn(*self.args, **self.kwargs)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.mThreadPool = QThreadPool()

        self.mCounter1= 0
        self.mCounter2 = 0

        self.layout = QVBoxLayout()

        self.startBtn = QPushButton('Start')
        self.startBtn.pressed.connect(self.start_incrementing)
        self.counterLabel1 = QLabel('Counter: 0')
        self.counterLabel2 = QLabel('Counter: 0')

        self._add_widgets_to_layout()

        win = QWidget()
        win.setLayout(self.layout)

        self.setCentralWidget(win)
        self.show()

    def start_incrementing(self):
        worker1 = ExWorker(self.increment_counter_one, max_counter=10)
        self.mThreadPool.start(worker1)
        
        worker2 = ExWorker(self.increment_counter_two, max_counter=10)
        self.mThreadPool.start(worker2)

    def increment_counter_one(self, max_counter=10):
        print("INcrementing")
        for i in range(max_counter):
            time.sleep(0.5)
            self.mCounter1 += 1
            self.counterLabel1.setText(f'Counter: {self.mCounter1}')

    def increment_counter_two(self, max_counter=10):
        print("INcrementing")
        for i in range(max_counter):
            time.sleep(0.1)
            self.mCounter2 += 1
            self.counterLabel2.setText(f'Counter: {self.mCounter2}')

    

    def _add_widgets_to_layout(self):

        self.layout.addWidget(self.startBtn)
        self.layout.addWidget(self.counterLabel1)
        self.layout.addWidget(self.counterLabel2)

if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    app.exec_()
