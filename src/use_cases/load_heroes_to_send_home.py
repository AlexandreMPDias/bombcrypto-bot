from cv2 import cv2
from os import listdir
from src.use_cases.utils import UseCase


class LoadHeroesToSendHome(UseCase):

    def handle(self):
        """Loads the images in the path and saves them as a list"""
        file_names = listdir('./targets/heroes-to-send-home')
        heroes = []
        for file in file_names:
            path = './targets/heroes-to-send-home/' + file
            heroes.append(cv2.imread(path))

        print('>>---> %d heroes that should be sent home loaded' % len(heroes))
        return heroes
