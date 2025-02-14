from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

from config import *

class BookViewr(object):
    def __init__(self, bookData = None  ) -> object:
        self.bookData = bookData

        self.app = QApplication(sys.argv)
        self.app.setStyle('Fusion')

        self.content = QWidget()
        self.content.show()
        # self.content.setFixedSize(300,300)
        self.text_font = QFont("Times font", TEXT_SIZE)
        self.text_height = QFontMetrics(self.text_font)

        self.text = QVBoxLayout(self.content)
        self.content.setLayout(self.text)

        self.j = 0

        self.next_page()

    def start(self):
        self.app.exec_()



    def next_page(self):

        for i in range(self.text.count()): self.text.itemAt(i).widget().close()

        self.btn = QPushButton(text = ">")
        self.btn.clicked.connect(self.next_page)
        self.text.addWidget(self.btn)



        k = 0
        while k < self.content.height():
            string = QLabel(f"{self.bookData[self.j]}")
            string.setFont(self.text_font)
            string.setWordWrap(True)
            self.text.addWidget(string)
            k += string.sizeHint().height() + LINE_SPACING
            self.j += 1

        self.btn = QPushButton(text = "<")
        self.btn.clicked.connect(self.prev_page)
        self.text.addWidget(self.btn)

    def prev_page(self):

        if self.j > 0:

            for i in range(self.text.count()): self.text.itemAt(i).widget().close()

            self.btn = QPushButton(text = ">")
            self.btn.clicked.connect(self.next_page)
            self.text.addWidget(self.btn)



            k = 0
            while k < self.content.height() and self.j > 0:
                string = QLabel(f"{self.bookData[self.j]}")
                string.setFont(self.text_font)
                string.setWordWrap(True)
                self.text.addWidget(string)
                k += string.sizeHint().height()
                self.j -= 1

            self.btn = QPushButton(text = "<")
            self.btn.clicked.connect(self.prev_page)
            self.text.addWidget(self.btn)

        else:
            return 1