import json

from src.styles.WhiteTheme import *
from src.styles.ConsoleTheme import *
from src.styles.DarkTheme import *
class configParser():

    def __init__(self, configName = "config.json", encoding = "utf-8"):
        self.data = json.load(open(configName, "r", encoding = encoding))

        self.WINDOW_NAME = self.data["WINDOW_NAME"]
        self.TEXT_SIZE = self.data["TEXT_SIZE"]
        self.FONT_NAME = self.data["FONT_NAME"]
        self.WINDOW_NAME = self.data["WINDOW_STYLE"]
        self.APP_THEME = self.data["APP_THEME"]
        match self.APP_THEME:
            case "white":
                self.APP_THEME = WhiteTheme.style
            case "dark":
                self.APP_THEME = DarkTheme.style
            case "console":
                self.APP_THEME = ConsoleTheme.style