import time


class __Format:
    def timestamp(self, format='%Y-%m-%d %H:%M:%S'):
        datetime = time.localtime()
        formatted = time.strftime(format, datetime)
        return formatted


Format = __Format()
