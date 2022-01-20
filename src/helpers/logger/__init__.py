from src.helpers.logger.load import LoggerHelper
from src.helpers.format import Format


class __Logger:
    def __init__(self):
        self.__helper = LoggerHelper()

    def log(self, message, progress_indicator=False, color='default'):

        if progress_indicator:
            if not self.__helper.last_log_is_progress:
                self.__helper.last_log_is_progress = True
                fmt_message = self.__helper.timestamp(
                    color, '⬆️ Processing last action..')
                self.__helper.write(fmt_message)
            else:
                self.__helper.write(self.__helper.paint(color, '.'))
            return

        if self.__helper.last_log_is_progress:
            self.__helper.write('\n')
            self.__helper.last_log_is_progress = False

        fmt_message = self.__helper.timestamp(None, message)
        print(self.__helper.paint(color, fmt_message))

        if (self.__helper.c['save_log_to_file'] == True):
            self.__helper.save("logs/logger.log", fmt_message + '\n')
        return True

    def mapClicked(self):
        self.log('🗺️ New Map button clicked!')
        self.__helper.save("logs/new-map.log", Format.timestamp() + '\n')


Logger = __Logger()
