from source.bookviewer import *
from source.Book import *
from source.styles.ConsoleTheme import *

if __name__ == "__main__":
    book = Book("samples/Отрочество Л.Н. Толстой.fb2", encoding="UTF-8")
    book.parse()
    app = BookViewer(book, appStyle = ConsoleTheme())
    app.start()
