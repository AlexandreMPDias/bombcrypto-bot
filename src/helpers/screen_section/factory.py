from src.helpers.config import Config
from src.helpers.screen_section import ScreenSection


class ScreenSectionFactory:
    def __init__(self, config: Config):
        self.__config = config

    def make(self, x, y, width, height) -> ScreenSection:
        return ScreenSection(x, y, width, height, self.__config)
