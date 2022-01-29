from src.helpers.config import Config
from src.helpers.logger import Logger
from src.comp_vision import CompVision
from src.ui_interaction.mouse_move import MouseMoveManager
import pyautogui


class ScrollManager:
    def __init__(self, gui: pyautogui, cv: CompVision, config: Config, move_manager: MouseMoveManager):
        self.__gui = gui
        self.__cv = cv
        self.__mv = move_manager

        self.use_click_and_drag_instead_of_scroll = config.use_click_and_drag_instead_of_scroll
        self.click_and_drag_amount = config.click_and_drag_amount
        self.scroll_size = config.scroll_size

    def heroes(self) -> None:
        commoms = self.__cv.positions('commom-text', threshold='commom')
        if (len(commoms) == 0):
            return
        x, y, w, h = commoms[len(commoms)-1]
        self.__mv.move(x, y, 1)

        if not self.use_click_and_drag_instead_of_scroll:
            self.__gui.scroll(-self.scroll_size)
        else:
            self.__gui.dragRel(0, -self.click_and_drag_amount,
                               duration=1, button='left')
