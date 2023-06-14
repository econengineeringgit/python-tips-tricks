import sys
import time
import threading

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import \
    QApplication, QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton

def readLogFile(fp):
    fp.seek(0, 2)
    while True:
        line = fp.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def Fibonacci(n, results, threadIdx):
    time.sleep(1)
    if n == 0:
        with open(".results", "a") as fp:
            fp.write(f"End.")
        return

    sequence = [0, 1]
    while len(sequence) <= n:
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(next_value)
    with open(".results", "a") as fp:
        fp.write(f"Thread: {threadIdx}, value: {sequence[-1]}\n")

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
        self.fibCounter = FibCounter()
        self.fibCounter.message.connect(self.updateText)
        self.fibCounter.finished.connect(lambda : self.logger.setText(self.logger.toPlainText() + "\n" + "Calculation finished..."))
        self.fibCounter.start()

    def updateText(self, mes):
        self.logger.setText(self.logger.toPlainText() + mes)    

class FibCounter(QThread):
    message = pyqtSignal(str)
    finished = pyqtSignal()
    results: list = []

    def run(self):
        inputs = [31, 32, 33, 34, 35, 0]
        
        with open(".results", "w"):
            pass
        threading.Thread(target=self.readLog).start()

        for inpIdx, inp in enumerate(inputs):
            t = threading.Thread(target=Fibonacci, args=(inp, self.results, inpIdx))
            t.start()
    
    def readLog(self):
        with open(".results", "r") as fp:
            logLines = readLogFile(fp)
            for line in logLines:
                if line == "End.":
                    break
                self.message.emit(line)
        self.finished.emit()

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())
