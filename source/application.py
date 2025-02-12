from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys

from config import *

class application:
    def __init__(self, bookData = None  ) -> object:
        self.app = QApplication(sys.argv)

        self.window = QScrollArea()
        self.window.setWidgetResizable(True)
        self.window.setWindowTitle(WINDOW_NAME)
        self.window.setWindowIcon(QtGui.QIcon('./media/karfagen.png'))
        self.window.setMinimumSize(MIN_WINDOW_X, MIN_WINDOW_Y)
        self.window.setMaximumSize(MAX_WINDOW_X, MAX_WINDOW_Y)
        self.window.show()

        self.content = QWidget()
        self.text = QVBoxLayout(self.content)
        string = QLabel("<br>".join(bookData))
        string.setWordWrap(True)
        self.text.addWidget(string)
        self.text.addStretch(1)
        self.window.setWidget(self.content)

    def start(self):
        self.app.exec_()

application(bookData="ебля")