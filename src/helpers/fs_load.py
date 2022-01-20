from os import listdir
from cv2 import cv2
import pyautogui
import yaml


class __Loader:
    def __init__(self):
        pass

    def __remove_suffix(self, input_string, suffix):
        """Returns the input_string without the suffix"""
        if suffix and input_string.endswith(suffix):
            return input_string[:-len(suffix)]
        return input_string

    def images(self, dir_path='./targets/'):
        """ Programatically loads all images of dir_path as a key:value where the
            key is the file name without the .png suffix

        Returns:
            dict: dictionary containing the loaded images as key:value pairs.
        """

        file_names = listdir(dir_path)
        targets = {}
        for file in file_names:
            path = 'targets/' + file
            targets[self.__remove_suffix(file, '.png')] = cv2.imread(path)

        return targets

    def config(self):
        # Load config file.
        stream = open("config.yaml", 'r')
        config = yaml.safe_load(stream)
        stream.close()
        return config


Load = __Loader()
