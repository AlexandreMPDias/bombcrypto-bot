from src.helpers.screen_section import ScreenSection
from src.helpers.add_randomness import add_randomness
from random import random
import pyautogui


class MouseMoveManager:
    def __init__(self, gui: pyautogui):
        self.__gui = gui

    def __moveWrapper(self, x, y, t):
        # print(f"Moving mouse to [{x},{y}]")
        self.__gui.moveTo(x, y, t)

    def __move(self, x: int, y: int, t, randomness: bool = True) -> None:
        tX = add_randomness(x, 10) if randomness else x
        tY = add_randomness(y, 10) if randomness else y
        tT = (t+random()/2) if randomness else t
        self.__moveWrapper(tX, tY, tT)

    def to(self, screen_section: ScreenSection, time) -> None:
        coords = screen_section.get_center_coords()
        self.__move(coords.x, coords.y, time)
