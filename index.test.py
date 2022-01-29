# -*- coding: utf-8 -*-
from time import sleep
from src.main import config, images, cv, mouse


def locate_image():
    mouse.click.at('test')


def main():

    print('iterating')

    locate_image()
    # mouse._mv.move(-1920, 0, 1)
    # while True:

    #     sleep()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program interrupted')
