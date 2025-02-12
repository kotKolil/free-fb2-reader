from PyQt5.QtWidgets import *
import sys

from config import *

class application:
    def __init__(self, book_data: list) -> object:
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle(WINDOW_NAME)
        self.window.resize(WINDOW_START_X, WINDOW_START_Y)
        self.window.show()
        self.line = QScrollArea()
        print(book_data)
        for i in book_data:
            string = QLabel(i)
            string.setWordWrap(True)
            self.line.addWidget(string)

        self.window.setLayout(self.line)
    def start(self):
        self.app.exec_()
