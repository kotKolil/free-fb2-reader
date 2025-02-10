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
        self.lang = None
        self.author_last_name = None
        self.author_first_name = None


    def parse(self):
        with (open(self.filename, encoding=self.encoding) as document):
            document = parse(document)

            self.document = document
            self.genre = self.loadTagValueFromXML("genre")
            self.lang = self.loadTagValueFromXML("lang")
            self.author_last_name = self.loadTagValueFromXML("last-name")
            self.author_last_name = self.loadTagValueFromXML("first-name")

            paragraphs = document.getElementsByTagName("section")
            for paragraph in paragraphs:
                text_nodes = [
                    node.childNodes[0].nodeValue for node in paragraph.childNodes
                    if node.nodeName == 'p' and node.childNodes[0].nodeValue
                ]
            self.text_data = text_nodes
            return 1

    def loadTagValueFromXML(self, tag_name):
        try:
            tag = self.document.getElementsByTagName(tag_name)[0].childNodes[0].nodeValue
            return tag
        except IndexError:
            return ""