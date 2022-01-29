from src.helpers.config import Config


class _ScreenSectionCoordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class ScreenSection:
    def __init__(self, x, y, width, height, config: Config):
        self.x = x + config.screen.offset_x
        self.y = y + config.screen.offset_y
        self.w = width
        self.h = height

    def get_center_coords(self):
        x = self.x + (self.w / 2)
        y = self.y + (self.h / 2)
        return _ScreenSectionCoordinates(x, y)

    def __str__(self) -> str:
        center = self.get_center_coords()
        return f"ScreenSection(x={self.x}, y={self.y}, w={self.w}, h={self.h}) - [{center.x}, {center.y}]"
