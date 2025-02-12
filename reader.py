from source.application import *
from source.parser import *

if __name__ == "__main__":
    book = Book("samples/Отрочество Л.Н. Толстой.fb2", encoding="UTF-8")
    book.parse()
    app = application(book.text_data)
    app.start()
