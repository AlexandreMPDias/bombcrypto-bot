from src.helpers.screen_section import ScreenSection
from src.helpers.elapsed_time import ElapsedTime
from src.helpers.logger import Logger
from src.comp_vision import CompVision
from src.ui_interaction.mouse_move import MouseMoveManager
import pyautogui


class ClickManager:
    def __init__(self, gui: pyautogui, cv: CompVision, move_manager: MouseMoveManager):
        self.__gui = gui
        self.__cv = cv
        self.__mouseMove = move_manager

    def screenSection(self, screenSection: ScreenSection):
        self.__mouseMove.to(screenSection, 1)
        self.__gui.click()

    def at(self, img_key, timeout=3, threshold="default"):
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
            matches = self.__cv.getScreenSections(img_key, threshold=threshold)

            if(len(matches) == 0):
                has_timed_out = elapsed.checkTimeout('click', randomness=False)
                continue
            for match in matches:
                self.screenSection(match)
            return True

        return False
