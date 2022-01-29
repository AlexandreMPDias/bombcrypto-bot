from src.helpers.config import Config
from src.comp_vision import CompVision
from src.ui_interaction.mouse_move import MouseMoveManager
from src.ui_interaction.scroll import ScrollManager
from src.ui_interaction.click import ClickManager


import pyautogui


class MouseManager:
    def __init__(self, gui: pyautogui, cv: CompVision, config: Config):
        self.move = MouseMoveManager(gui)

        self.scroll = ScrollManager(gui, cv, config, self.move)
        self.click = ClickManager(gui, cv, self.move)
