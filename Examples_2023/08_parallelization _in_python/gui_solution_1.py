import sys
import threading

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import \
    QApplication, QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(560, 240, 800, 600)
        layout = QVBoxLayout()

        self.button = QPushButton("Click")
        self.button.clicked.connect(self.startFib)
        self.logger = QTextEdit()

        layout.addWidget(self.button)
        layout.addWidget(self.logger)
        self.setLayout(layout)

    def startFib(self):
        self.updateText("Calculation started...")
        self.fibCounter = FibCounter()
        self.fibCounter.message.connect(self.updateText)
        self.fibCounter.finished.connect(lambda : self.logger.setText(self.logger.toPlainText() + "\n" + "Calculation finished..."))
        self.fibCounter.start()

    def updateText(self, mes):
        self.logger.setText(self.logger.toPlainText() + "\n" + mes)

class FibCounter(QThread):
    message = pyqtSignal(str)
    finished = pyqtSignal()

    def run(self):
        inputs = [31, 32, 33, 34, 35]
        threads = []
        for inp in inputs:
            t = threading.Thread(target=Fibonacci, args=(inp, ))
            threads.append(t)
            t.start()
        for tIdx, t in enumerate(threads):
            t.join()
            self.message.emit(f"Thread: {tIdx} finished.")
        self.finished.emit()

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())