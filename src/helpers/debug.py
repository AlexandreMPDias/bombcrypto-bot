"""

DEBUG.PY

Used for code debugging.
Contains the following classes:
[** = not yet implemented]
    Log:
        error(String)           : returns self
        sucess(String)          : returns self
        warn(String)            : returns self
        info(String)            : returns self
        color(Color, String)    : returns self
        split(Color)            : returns self
        **critical(String)      : returns self
    
    IntegrityTest:
        isValidProcess(Process, String)      : returns True/False
        isCameraConnected(Boolean)           : returns True/False
        canLocateFile(String, String)        : returns True/False
        canLocateDir(String, String)         : returns True/False
        **isNone(Object, String)             : returns self
        **performInitialChecks()             : returns self
        hasInternetConnection() [not tested] : returns self

        

Requires installation of colorama: [ pip install colorama ]

Note: 
    -- Not designed to be Thread safe.
    -- Debug doesnt work yet

@Created by Padawan Alexandre

"""
import ctypes
try:
    import httplib
except:
    import http.client as httplib
import pathlib
import os
try:
    from colorama import init as _color_init
    from colorama import Fore, Back, Style
    _color_init()

    FONT_COLOR_RED = Fore.RESET+Fore.RED
    FONT_COLOR_GREEN = Fore.RESET+Fore.GREEN
    FONT_COLOR_RESET = Fore.RESET
    FONT_COLOR_YELLOW = Fore.RESET+Fore.YELLOW

    """
    Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Style: DIM, NORMAL, BRIGHT, RESET_ALL
    """
except:
    FONT_COLOR_RED = ''
    FONT_COLOR_GREEN = ''
    FONT_COLOR_RESET = ''
    FONT_COLOR_YELLOW = ''

# Debug Levels
LOG_SHOW_EVERYTHING = 2
LOG_SHOW_IMPORTANT_ONLY = 0
LOG_SHOW_INFO = 1
LOG_SHOW_NOTHING = -1


class Log():
    def __init__(self, debug_level=0):
        """

        """
        self._debug_level = debug_level

    def error(self, str: str):
        """
        Prints an error message on the console. [Error] colored RED
        """
        if self._debug_level == 0:
            self.__print(FONT_COLOR_RED +
                         '[ Erro ]: ' + FONT_COLOR_RESET + str)
        return self

    def success(self, str):
        """
        Prints a success message on the console. [Sucess] colored Green
        """
        if self._debug_level == 0:
            self.__print(FONT_COLOR_GREEN +
                         '[Sucess]: ' + FONT_COLOR_RESET + str)
        return self

    def info(self, str):
        """
        Prints an info message on the console. [Info] colored WHITE
        """
        if self._debug_level == 0:
            self.__print('[ Info ]: ' + str)
        return self

    def warn(self, str):
        """
        Prints an Warning message on the console. [Warn] colored WHITE
        """
        if self._debug_level == 0:
            self.__print(FONT_COLOR_YELLOW +
                         '[ Warn ]: ' + FONT_COLOR_RESET + str)
        return self

    def color(self, col="", str=''):
        """
        Prints a colored message on the console. The entire string colored @param col
        """
        if self._debug_level == 0:
            self.__print(col + str + FONT_COLOR_RESET)
        return self

    def split(self, col=""):
        """
        Draws a line on the console.
        """
        if self._debug_level == 0:
            self.color(col, "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        return self

    def __print(self, str):
        """
        Prints a message on the console.
        """
        print(str)


class Paint:
    @staticmethod
    def red(str: str) -> str:
        return FONT_COLOR_RED + str + FONT_COLOR_RESET

    @staticmethod
    def green(str: str) -> str:
        return FONT_COLOR_GREEN + str + FONT_COLOR_RESET

    @staticmethod
    def yellow(str: str) -> str:
        return FONT_COLOR_YELLOW + str + FONT_COLOR_RESET


log = Log()


def PopUp(header, text):
    """
    @Created by Padawan Alexandre

    Generates a PopUp Window on Windows based Systems
    @param: header    - Is the title on the Window
    @param: text    - Is the text content displayed inside the Window
    """
    try:
        ctypes.windll.user32.MessageBoxW(0, text, header, 0)
    except:
        log.warn(
            'PopUp method not found. Ignore this message if you\'re not using Windows')


class IntegrityTest():
    def __init__(self):
        pass

    def canLocateDir(self, path, createIfNotFound=False, hint=''):
        """
            Check if the path in the parameter { path } is a directory.
            @param createIfNotFound: is set to True, and the path does not point to
            a directory, the directory will be created.
        """
        found = self.__locator(path, os.path.isdir(path), hint)
        if not found and createIfNotFound:
            pathlib.Path(path).mkdir(parents=True, exist_ok=True)
        return found

    def canLocateFile(self, file, hint=''):
        """
        Check if the path in the parameter { file } is a file.
        """
        return self.__locator(file, os.path.isfile(file), hint)

    def hasInternetConnection(self):
        """
        Check there's an internet connection
        """
        if self.__have_internet():
            log.sucess('Internet Connection found')
            return True
        else:
            log.error('No Internet Connection')
            return False

    def __have_internet(self):
        """
        Checks if it is possible to connect to [www.google.com]
        """
        conn = httplib.HTTPConnection("www.google.com", timeout=5)
        try:
            conn.request("HEAD", "/")
            conn.close()
            return True
        except:
            conn.close()
            return False

    def __locator(self, path, found, hint):
        """
        Prints a message if a path points to something.
        """
        if found:
            log.sucess('[ {} ] found'.format(path))
            return True
        else:
            if not hint == '':
                log.error('[ {} ] not found\nHINT: {}'.format(path, hint))
            else:
                log.error('[ {} ] not found'.format(path))
            return False
