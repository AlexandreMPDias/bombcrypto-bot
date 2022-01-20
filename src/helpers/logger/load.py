from src.helpers.format import Format
from src.helpers.logger.colors import COLOR

import sys
import yaml


class LoggerHelper:
    def __init__(self):
        self.last_log_is_progress = False
        self.stream = open("./config.yaml", 'r')
        self.c = yaml.safe_load(self.stream)

    def write(self, message: str):
        sys.stdout.write(message)
        sys.stdout.flush()

    def save(self, file: str, message: str):
        logger_file = open(f"./{file}", "a", encoding='utf-8')
        logger_file.write(message)
        logger_file.close()

    def paint(self, color, message: str):
        color_formatted = COLOR.get(color.lower(), COLOR['default'])
        return color_formatted + message + '\033[0m'

    def timestamp(self, color, message: str):
        ts = Format.timestamp()
        fmt_message = "[{}] => {}".format(ts, message)
        if color is None:
            return fmt_message
        return self.paint(color, fmt_message)
