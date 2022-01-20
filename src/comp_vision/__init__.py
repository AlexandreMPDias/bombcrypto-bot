from cv2 import cv2
import numpy as np
from src.helpers.config import Config
from src.helpers.images import Images

from src.comp_vision.print_screen import PrintScreen


class CompVision:
    def __init__(self, config: Config, images: Images):
        self.__ct = config.thresholds.values
        self.__printScrn = PrintScreen()
        self.__images = images

    def positions(self, target, threshold=None, img=None) -> list:
        th = self.__getThreshold(threshold)

        if img is None:
            img = self.__printScrn.take()

        target_img = self.__images.get(target)

        result = cv2.matchTemplate(img, target_img, cv2.TM_CCOEFF_NORMED)
        w = target_img.shape[1]
        h = target_img.shape[0]

        yloc, xloc = np.where(result >= th)

        rectangles = []
        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), int(w), int(h)])
            rectangles.append([int(x), int(y), int(w), int(h)])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        return rectangles

    def __getThreshold(self, value):
        if(value is None):
            return self.__ct['default']
        if value in self.__ct:
            return self.__ct[value]
        if type(value) is str:
            raise Exception(f"Invalid threshold value: {value}")
        return value
