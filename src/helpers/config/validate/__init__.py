from src.helpers.config.config_instance import ConfigInstance
from src.helpers.config.validate.rules import ConfigValidationRule


class ConfigValidation(ConfigInstance):
    def __init__(self, source, path) -> None:
        self.__source = source
        self.__path = path

    def compose(self, key):
        return ConfigValidationRule(key, self.__path, self.__source)
