from src.helpers.globals import Globals
from src.helpers.config import Config
from src.helpers.images import Images
from src.helpers.fs_load import Load
import pyautogui


from src.comp_vision import CompVision
from src.ui_interaction import MouseManager

globalValues = Globals()
config = Config(Load.config())
images = Images(Load.images())
cv = CompVision(config=config, images=images)
mouse = MouseManager(gui=pyautogui, cv=cv, config=config)
