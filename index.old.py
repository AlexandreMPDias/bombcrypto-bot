# -*- coding: utf-8 -*-
from src.helpers.elapsed_time import ElapsedTime
from src.helpers.banner import banner
from src.helpers.fs_load import Load
from src.helpers.logger import Logger
from cv2 import cv2
from os import listdir
from random import randint
import numpy as np
import mss
import pyautogui
import time
import sys
from src.main import config, images, cv, mouse, globalValues

# Load config file.
c = Load.config()
ct = c['threshold']
ch = c['home']
pause = c['time_intervals']['interval_between_moviments']
pyautogui.PAUSE = pause


def loadHeroesToSendHome():
    """Loads the images in the path and saves them as a list"""
    file_names = listdir('./targets/heroes-to-send-home')
    heroes = []
    for file in file_names:
        path = './targets/heroes-to-send-home/' + file
        heroes.append(cv2.imread(path))

    print('>>---> %d heroes that should be sent home loaded' % len(heroes))
    return heroes


def show(rectangles, img=None):
    """ Show an popup with rectangles showing the rectangles[(x, y, w, h),...]
        over img or a printSreen if no img provided. Useful for debugging"""

    if img is None:
        with mss.mss() as sct:
            monitor = sct.monitors[0]
            img = np.array(sct.grab(monitor))

    for (x, y, w, h) in rectangles:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255, 255), 2)

    # cv2.rectangle(img, (result[0], result[1]), (result[0] + result[2], result[1] + result[3]), (255,50,255), 2)
    cv2.imshow('img', img)
    cv2.waitKey(0)


def clickButtons():
    buttons = cv.positions('go-work', threshold='go_to_work_btn')
    # print('buttons: {}'.format(len(buttons)))
    for (x, y, w, h) in buttons:
        mouse.move(x+(w/2), y+(h/2), 1)
        pyautogui.click()
        global hero_clicks
        hero_clicks = hero_clicks + 1
        # cv2.rectangle(sct_img, (x, y) , (x + w, y + h), (0,255,255),2)
        if hero_clicks > 20:
            Logger.log(
                'too many hero clicks, try to increase the go_to_work_btn threshold')
            return
    return len(buttons)


def isHome(hero, buttons):
    y = hero[1]

    for (_, button_y, _, button_h) in buttons:
        isBelow = y < (button_y + button_h)
        isAbove = y > (button_y - button_h)
        if isBelow and isAbove:
            # if send-home button exists, the hero is not home
            return False
    return True


def isWorking(bar, buttons):
    y = bar[1]

    for (_, button_y, _, button_h) in buttons:
        isBelow = y < (button_y + button_h)
        isAbove = y > (button_y - button_h)
        if isBelow and isAbove:
            return False
    return True


def clickGreenBarButtons():
    # ele clicka nos q tao trabaiano mas axo q n importa
    offset = 140

    green_bars = cv.positions('green-bar', threshold=ct['green_bar'])
    Logger.log('🟩 %d green bars detected' % len(green_bars))
    buttons = cv.positions('go-work', threshold=ct['go_to_work_btn'])
    Logger.log('🆗 %d buttons detected' % len(buttons))

    not_working_green_bars = []
    for bar in green_bars:
        if not isWorking(bar, buttons):
            not_working_green_bars.append(bar)
    if len(not_working_green_bars) > 0:
        Logger.log('🆗 %d buttons with green bar detected' %
                   len(not_working_green_bars))
        Logger.log('👆 Clicking in %d heroes' % len(not_working_green_bars))

    # se tiver botao com y maior que bar y-10 e menor que y+10
    hero_clicks_cnt = 0
    for (x, y, w, h) in not_working_green_bars:
        # isWorking(y, buttons)
        mouse.move(x+offset+(w/2), y+(h/2), 1)
        pyautogui.click()
        global hero_clicks
        hero_clicks = hero_clicks + 1
        hero_clicks_cnt = hero_clicks_cnt + 1
        if hero_clicks_cnt > 20:
            Logger.log(
                '⚠️ Too many hero clicks, try to increase the go_to_work_btn threshold')
            return
        # cv2.rectangle(sct_img, (x, y) , (x + w, y + h), (0,255,255),2)
    return len(not_working_green_bars)


def clickFullBarButtons():
    offset = 100
    full_bars = positions('full-stamina', threshold=ct['default'])
    buttons = positions('go-work', threshold=ct['go_to_work_btn'])

    not_working_full_bars = []
    for bar in full_bars:
        if not isWorking(bar, buttons):
            not_working_full_bars.append(bar)

    if len(not_working_full_bars) > 0:
        Logger.log('👆 Clicking in %d heroes' % len(not_working_full_bars))

    for (x, y, w, h) in not_working_full_bars:
        mouse.move(x+offset+(w/2), y+(h/2), 1)
        pyautogui.click()
        global hero_clicks
        hero_clicks = hero_clicks + 1

    return len(not_working_full_bars)


def goToHeroes():
    if mouse.click('go-back-arrow'):
        global login_attempts
        login_attempts = 0

    # TODO tirar o sleep quando colocar o pulling
    time.sleep(1)
    mouse.click('hero-icon')
    time.sleep(randint(1, 3))


def goToGame():
    # in case of server overload popup
    mouse.click('x')
    # time.sleep(3)
    mouse.click('x')

    mouse.click('treasure-hunt-icon')


def refreshHeroesPositions():

    Logger.log('🔃 Refreshing Heroes Positions')
    mouse.click('go-back-arrow')
    mouse.click('treasure-hunt-icon')

    # time.sleep(3)
    mouse.click('treasure-hunt-icon')


def login():
    global login_attempts
    Logger.log('😿 Checking if game has disconnected')

    if login_attempts > 3:
        Logger.log('🔃 Too many login attempts, refreshing')
        login_attempts = 0
        pyautogui.hotkey('ctrl', 'f5')
        return

    if mouse.click('connect-wallet', timeout=10):
        Logger.log('🎉 Connect wallet button detected, logging in!')
        login_attempts = login_attempts + 1
        # TODO mto ele da erro e poco o botao n abre
        # time.sleep(10)

    if mouse.click('select-wallet-2', timeout=8):
        # sometimes the sign popup appears imediately
        login_attempts = login_attempts + 1
        # print('sign button clicked')
        # print('{} login attempt'.format(login_attempts))
        if mouse.click('treasure-hunt-icon', timeout=15):
            # print('sucessfully login, treasure hunt btn clicked')
            login_attempts = 0
        return
        # click ok button

    if not mouse.click('select-wallet-1-no-hover', ):
        if mouse.click('select-wallet-1-hover', threshold=ct['select_wallet_buttons']):
            pass
            # o ideal era que ele alternasse entre checar cada um dos 2 por um tempo
            # print('sleep in case there is no metamask text removed')
            # time.sleep(20)
    else:
        pass
        # print('sleep in case there is no metamask text removed')
        # time.sleep(20)

    if mouse.click('select-wallet-2', timeout=20):
        login_attempts = login_attempts + 1
        # print('sign button clicked')
        # print('{} login attempt'.format(login_attempts))
        # time.sleep(25)
        if mouse.click('treasure-hunt-icon', timeout=25):
            # print('sucessfully login, treasure hunt btn clicked')
            login_attempts = 0
        # time.sleep(15)

    if mouse.click('ok', timeout=5):
        pass
        # time.sleep(15)
        # print('ok button clicked')


def sendHeroesHome():
    if not ch['enable']:
        return
    heroes_positions = []
    for hero in home_heroes:
        hero_positions = cv.positions(hero, threshold=ch['hero_threshold'])
        if not len(hero_positions) == 0:
            # TODO maybe pick up match with most wheight instead of first
            hero_position = hero_positions[0]
            heroes_positions.append(hero_position)

    n = len(heroes_positions)
    if n == 0:
        print('No heroes that should be sent home found.')
        return
    print(' %d heroes that should be sent home found' % n)
    # if send-home button exists, the hero is not home
    go_home_buttons = cv.positions(
        'send-home', threshold=ch['home_button_threshold'])
    # TODO pass it as an argument for both this and the other function that uses it
    go_work_buttons = cv.positions(
        'go-work', threshold=ct['go_to_work_btn'])

    for position in heroes_positions:
        if not isHome(position, go_home_buttons):
            print(isWorking(position, go_work_buttons))
            if(not isWorking(position, go_work_buttons)):
                print('hero not working, sending him home')
                mouse.move(
                    go_home_buttons[0][0]+go_home_buttons[0][2]/2, position[1]+position[3]/2, 1)
                pyautogui.click()
            else:
                print('hero working, not sending him home(no dark work button)')
        else:
            print('hero already home, or home full(no dark home button)')


def refreshHeroes():
    Logger.log('🏢 Search for heroes to work')

    goToHeroes()

    if c['select_heroes_mode'] == "full":
        Logger.log('⚒️ Sending heroes with full stamina bar to work', 'green')
    elif c['select_heroes_mode'] == "green":
        Logger.log('⚒️ Sending heroes with green stamina bar to work', 'green')
    else:
        Logger.log('⚒️ Sending all heroes to work', 'green')

    buttonsClicked = 1
    empty_scrolls_attempts = c['scroll_attemps']

    while(empty_scrolls_attempts > 0):
        if c['select_heroes_mode'] == 'full':
            buttonsClicked = clickFullBarButtons()
        elif c['select_heroes_mode'] == 'green':
            buttonsClicked = clickGreenBarButtons()
        else:
            buttonsClicked = clickButtons()

        sendHeroesHome()

        if buttonsClicked == 0:
            empty_scrolls_attempts = empty_scrolls_attempts - 1
        mouse.scroll()
        time.sleep(2)
    Logger.log('💪 {} heroes sent to work'.format(hero_clicks))
    goToGame()


def main():
    """Main execution setup and loop"""
    # ==Setup==
    global hero_clicks
    global login_attempts
    global last_log_is_progress
    hero_clicks = 0
    login_attempts = 0
    last_log_is_progress = False

    global images
    images = Load.images()
    mouse.images = images

    if ch['enable']:
        global home_heroes
        home_heroes = loadHeroesToSendHome()
    else:
        print('>>---> Home feature not enabled')
    print('\n')

    print(banner)
    # time.sleep(7)
    t = c['time_intervals']

    # =========
    timeout = ElapsedTime({
        "check_for_login": 0,
        "send_heroes_for_work": 0,
        "check_for_new_map_button": 0,
        "check_for_captcha": 0,
        "refresh_heroes_positions": 0
    })

    while True:
        timeout.checkTimeout('check_for_captcha')

        if timeout.checkTimeout('send_heroes_for_work'):
            refreshHeroes()

        if timeout.checkTimeout('check_for_login'):
            sys.stdout.flush()
            login()

        # if timeout.checkTimeout('check_for_new_map_button') and mouse.click('new-map'):
        if timeout.checkTimeout('check_for_new_map_button') and mouse.click('new-map'):
            Logger.mapClicked()

        if timeout.checkTimeout('refresh_heroes_positions'):
            refreshHeroesPositions()

        Logger.log(None, progress_indicator=True)

        sys.stdout.flush()

        time.sleep(1)


if __name__ == '__main__':
    main()


# cv2.imshow('img',sct_img)
# cv2.waitKey()

# colocar o botao em pt
# soh resetar posiçoes se n tiver clickado em newmap em x segundos
