from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from source.Book import *
from source.styles.style import *
from source.styles.WhiteTheme import *

import sys
from config import *


class BookViewer(object):
    def __init__(self, bookData: Book, appStyle: style = WhiteTheme, appStyleFromSystem="Windows",
                 app=QApplication(sys.argv)) -> None:

        self.app = app

        # getting data from Book object
        self.Book = bookData
        self.bookData = bookData.text_data

        # creating and configuring BookViewer window
        self.content = QWidget()
        self.content.setFixedSize(500, 500)
        self.content.setWindowIcon(QIcon("./media/karfagen.png"))
        self.content.setWindowTitle(f"{self.Book.title} {self.Book.author} - Karfagen Book Viewer")
        self.content.setStyleSheet(appStyle.style)
        self.text_font = QFont(FONT_NAME, TEXT_SIZE)
        self.text_height = QFontMetrics(self.text_font)

        self.layout = QVBoxLayout(self.content)

        self.pageNumber = 0

        self.textLabel = QLabel()
        self.textLabel.setWordWrap(1)
        self.textLabel.resize(400, 400)

        self.layout.addWidget(self.textLabel)
        self.navigationBox = QGroupBox()
        self.navigationBox.setStyleSheet("""
        QGroupBox {
            border: 0px black solid;
        }
        """)

        self.navigationBoxLayout = QHBoxLayout()

        self.btn_prev = QPushButton(text="<")
        self.btn_prev.clicked.connect(self.prev_page)

        self.pageNumberLabel = QLabel(text=str(self.pageNumber))

        self.btn_next = QPushButton(text=">")
        self.btn_next.clicked.connect(self.next_page)

        self.navigationBoxLayout.addWidget(self.btn_prev)
        self.navigationBoxLayout.addWidget(self.pageNumberLabel)
        self.navigationBoxLayout.addWidget(self.btn_next)

        self.navigationBox.setLayout(self.navigationBoxLayout)

        self.layout.addStretch()
        self.layout.addWidget(self.navigationBox)

        self.content.setLayout(self.layout)

        self.pages = self.parseBookData()

        self.render_page(self.pageNumber)

    def start(self):
        self.content.show()
        self.app.exec_()

    def render_page(self, pageNumber):
        try:
            self.pageNumberLabel.setText(str(pageNumber + 1))
            self.textLabel.setText("".join(self.pages[self.pageNumber]))
        except Exception as e:
            self.show_messagebox(str(e))

    def prev_page(self):
        if self.pageNumber > 0:
            self.pageNumber -= 1
            self.render_page(self.pageNumber)

    def next_page(self):
        if self.pageNumber <= len(self.pages):
            self.pageNumber += 1
            print(self.pageNumber)
            self.render_page(self.pageNumber)

    def parseBookData(self):
        """
        Parses raw book data into pages, handling paragraph wrapping and page breaks.

        Returns:
            A list of pages, where each page is a list of strings (paragraphs/lines).
        """

        pages= []
        page = []
        current_text_height = 0
        font_metrics = QFontMetrics(QFont(FONT_NAME, TEXT_SIZE))

        for paragraph in self.Book.text_data:
            # Split paragraph into lines that fit
            lines = self.split_paragraph_into_lines(paragraph, font_metrics, self.textLabel.width())
            for line in lines:
                line_height = font_metrics.height()  # Use actual line height

                if current_text_height + line_height <= self.textLabel.height():
                    page.append(line + "<br>")
                    current_text_height += line_height
                else:
                    pages.append(page)
                    page = [line]
                    current_text_height = line_height  # Reset height to the current line's height

        # Add the last page if it's not empty
        if page:
            pages.append(page)

        return pages

    def split_paragraph_into_lines(self, paragraph: str, font_metrics: QFontMetrics, max_width: int):
        """
        Splits a paragraph into lines that fit within the maximum width, handling word wrapping.

        Args:
            paragraph: The paragraph to split.
            font_metrics: QFontMetrics object.
            max_width: The maximum width for a line.

        Returns:
            A list of strings, where each string is a line.
        """

        if font_metrics.horizontalAdvance(paragraph) >= self.textLabel.width():

            words = paragraph.split()
            lines = []
            current_line = ""

            for word in words:
                test_line = current_line + word + " "  # Add word and a space to test
                if font_metrics.horizontalAdvance(test_line) <= max_width:
                    current_line = test_line
                else:
                    if current_line:  # Add the current line if it's not empty
                        newString = ""
                        for i in range(len(current_line)):
                            newString += current_line[i]
                            if font_metrics.horizontalAdvance(newString) == max_width:
                                break
                    lines.append(newString)
                    current_line = word + " " + current_line[i:len(current_line)]  # Start a new line with the current word

            if current_line:  # Add the last line
                lines.append(current_line.strip())
            return lines

        else:
            return [paragraph]

    def show_messagebox(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Error)
        msg.setText(text)
        msg.setInformativeText("")
        msg.setWindowTitle("error")
        msg.setDetailedText("")
        msg.exec()