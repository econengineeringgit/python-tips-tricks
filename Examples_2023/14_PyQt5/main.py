import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from example import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.button_input.clicked.connect(lambda: print("input"))
        self.button_output.clicked.connect(lambda: print("output"))
        self.button_convert.clicked.connect(lambda: print("convert"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())