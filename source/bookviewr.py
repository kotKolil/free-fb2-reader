from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from source.Book import *
from source.styles.style import *
from source.styles.WhiteTheme import *

import sys
from config import *

class BookViewr(object):
    def __init__(self, bookData: Book, appStyle : style =  WhiteTheme, appStyleFromSystem = "Windows") -> None:
        self.Book = bookData
        self.bookData = bookData.text_data

        self.app = QApplication(sys.argv)
        self.app.setStyle(appStyleFromSystem)

        self.content = QWidget()
        self.content.setFixedSize(600,600)
        self.content.setWindowIcon(QIcon("./media/karfagen.png"))
        self.content.setWindowTitle(f"{self.Book.title} {self.Book.author} - Karfagen Book Viewer")
        self.content.setStyleSheet(appStyle.style)
        self.text_font = QFont("Times New Roman", TEXT_SIZE)
        self.text_height = QFontMetrics(self.text_font)

        self.text = QVBoxLayout(self.content)
        self.navigationBottom = QHBoxLayout(self.content)
        self.content.setLayout(self.text)
        self.content.setLayout(self.navigationBottom)

        self.pageNumber = 0
        self.latestRenderedParagraph = 0
        self.pageData = {
            0: [],
        }

        self.navigationBox = QGroupBox()
        self.navigationBoxLayout = QHBoxLayout()
        self.navigationBox.setStyleSheet("""
        QGroupBox
            {
                border: 0px black solid;
            }
        """)
        self.navigationBox.setFixedHeight(50)
        self.navigationBoxLayout.addStretch(1)
        self.navigationBox.setLayout(self.navigationBoxLayout)

        self.btn_next = QPushButton(text=">")
        self.btn_next.clicked.connect(self.next_page)
        self.text.addWidget(self.btn_next)

        self.pageNumberLabel = QLabel(text=str(self.pageNumber))
        self.navigationBoxLayout.addWidget(self.pageNumberLabel)

        self.btn_prev = QPushButton(text="<")
        self.btn_prev.clicked.connect(self.prev_page)
        self.navigationBottom.addWidget(self.btn_prev)

        self.navigationBoxLayout.addWidget(self.btn_prev)
        self.navigationBoxLayout.addWidget((self.btn_next))
        self.text.addWidget(self.navigationBox)

    def start(self):
        self.content.show()
        self.app.exec_()

    def render_page(self, pageNumber):
        if pageNumber > 0:
            if not pageNumber in self.pageData:
                textHeight = 0
                paragpaphs = []
                self.latestRenderedParagraph += 1
                while textHeight < self.content.height():
                    label = QLabel(text = self.bookData[self.latestRenderedParagraph])
                    label.setWordWrap(True)
                    self.text.addWidget(label)

                    text = self.bookData[self.latestRenderedParagraph]
                    textHeight += label.height()
                self.pageNumber += 1
                self.pageData[self.pageNumber] = paragpaphs
            else:
                for paragraph in self.pageData[self.j]:
                    label = QLabel(text = paragraph)
                    label.setWordWrap(True)
                    self.text.addWidget(label)
    def prev_page(self):
        self.render_page(self.pageNumber - 1)

    def next_page(self):
        self.render_page(self.pageNumber + 1)

