from cv2 import cv2
import numpy as np
from typing import List

from src.helpers.config import Config
from src.helpers.images import Images
from src.helpers.screen_section import ScreenSection
from src.helpers.screen_section.factory import ScreenSectionFactory
from src.comp_vision.print_screen import PrintScreen


class CompVision:
    def __init__(self, config: Config, images: Images):
        self.__ct = config.thresholds
        self.__printScrn = PrintScreen()
        self.__images = images
        self.__scrnFactory = ScreenSectionFactory(config)

    def positions(self, target, threshold=None, img=None) -> list:
        th = self.__getThreshold(threshold)

        if img is None:
            img = self.__printScrn.take()

        target_img = self.__images.get(target)

        result = cv2.matchTemplate(img, target_img, cv2.TM_CCOEFF_NORMED)
        w = target_img.shape[1]
        h = target_img.shape[0]

        yloc, xloc = np.where(result >= th)

        print(xloc, yloc)

        rectangles = []
        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), int(w), int(h)])
            rectangles.append([int(x), int(y), int(w), int(h)])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        return rectangles

    def getScreenSections(self, target, threshold=None, img=None) -> List[ScreenSection]:
        rects = self.positions(target, threshold, img)

        print(rects)

        matches = []
        for (x, y, w, h) in rects:
            matches.append(self.__scrnFactory.make(x, y, w, h))

        return matches

    def __getThreshold(self, value):
        if(value is None):
            return self.__ct['default']
        if type(value) is int or type(value) is float:
            return value
        if value in self.__ct:
            return self.__ct[value]
        if type(value) is str:
            raise Exception(f"Invalid threshold value: {value}")
        return value
