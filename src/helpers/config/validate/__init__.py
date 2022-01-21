from src.helpers.config.validate.rules import ConfigValidationRule


class ConfigValidation:
    def __init__(self, source, path) -> None:
        self.__source = source
        self.__path = path

    def compose(self, key):
        value = self.__source[key]
        return ConfigValidationRule(key, value, self.__path, self.__source)
