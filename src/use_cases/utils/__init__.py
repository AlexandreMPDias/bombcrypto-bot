from src.helpers.globals import Globals
from src.comp_vision import CompVision
from src.ui_interaction import MouseManager


class UseCase:
    def __init__(self, cv: CompVision, mouse: MouseManager, globals: Globals):
        self.cv = cv
        self.mouse = mouse
        self.globals = globals
