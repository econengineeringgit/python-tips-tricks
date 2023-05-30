import sys
import threading

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
        inputs = [31, 32, 33, 34, 35]
        threads = []
        for inp in inputs:
            t = threading.Thread(target=Fibonacci, args=(inp, ))
            threads.append(t)
            t.start()
        for tIdx, t in enumerate(threads):
            t.join()
            self.logger.setText(self.logger.toPlainText() + "\n" + f"Thread: {tIdx} finished.")

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())