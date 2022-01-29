from src.helpers.elapsed_time import ElapsedTime
from src.helpers.config import Config
from src.helpers.logger import Logger
from src.comp_vision import CompVision
from src.helpers.add_randomness import add_randomness
from random import random
import pyautogui


class ClickManager:
    def __init__(self, gui: pyautogui, cv: CompVision, config: Config):
        self.__gui = gui
        self.__cv = cv

        self.use_click_and_drag_instead_of_scroll = config.use_click_and_drag_instead_of_scroll
        self.click_and_drag_amount = config.click_and_drag_amount
        self.scroll_size = config.scroll_size

    def move(self, x: int, y: int, t, randomness: bool = True) -> None:
        tX = add_randomness(x, 10) if randomness else x
        tY = add_randomness(y, 10) if randomness else y
        tT = (t+random()/2) if randomness else t
        self.__gui.moveTo(tX, tY, tT)

    def scroll(self) -> None:
        commoms = self.__cv.positions('commom-text', threshold='commom')
        if (len(commoms) == 0):
            return
        x, y, w, h = commoms[len(commoms)-1]
        self.move(x, y, 1)

        if not self.use_click_and_drag_instead_of_scroll:
            self.__gui.scroll(-self.scroll_size)
        else:
            self.__gui.dragRel(0, -self.click_and_drag_amount,
                               duration=1, button='left')

    def click(self, img_key, timeout=3, threshold='default'):
        """Search for img in the screen, if found moves the cursor over it and clicks.
        Parameters:
            img: The key of the image that will be used as an template to find where to click.
            timeout (int): Time in seconds that it will keep looking for the img before returning with fail
            threshold(float): How confident the bot needs to be to click the buttons (values from 0 to 1)
        """
        Logger.log(None, progress_indicator=True)
        elapsed = ElapsedTime({'click': timeout})
        has_timed_out = False
        while (not has_timed_out):
            matches = self.__cv.positions(img_key, threshold=threshold)

            if(len(matches) == 0):
                has_timed_out = elapsed.checkTimeout('click', randomness=False)
                continue

            x, y, w, h = matches[0]
            pos_click_x = x+w/2
            pos_click_y = y+h/2
            self.move(pos_click_x, pos_click_y, 1)
            self.__gui.click()
            return True

        return False
