from source.application import application
from source.parser import *
#from source.application import *

if __name__ == "__main__":
    book = Book("samples/Отрочество Л.Н. Толстой.fb2", encoding="UTF-8")
    data = book.parse

    app = application()
    app
