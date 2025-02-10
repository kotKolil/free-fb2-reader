from xml.dom.minidom import parse


class Book(object):

    def __init__(self, filename, encoding="UTF-8"):
        self.filename = filename
        self.encoding = encoding

        self.text_data = None
        self.document = None

        self.genre = None
        self.author = None
        self.title = None

    def parse(self):
        with open(self.filename, encoding=self.encoding) as document:
            document = parse(document)
            self.document = document
            self.genre = document.getElementsByTagName("genre")[0].childNodes[0].nodeValue
            paragraphs = document.getElementsByTagName("section")
            for paragraph in paragraphs:
                text_nodes = [
                    node.childNodes[0].nodeValue for node in paragraph.childNodes
                    if node.nodeName == 'p' and node.childNodes[0].nodeValue
                ]
            self.text_data = text_nodes
            return 1