
def __invalid(rule, message: str):
    path = f"{rule.__path}.{rule.key}"
    raise ValueError(
        f"Invalid Configuration value {rule.value} for {path} found in config.yaml: {message}")


class ConfigValidationRule:
    def __init__(self, key: str, value, path: str, source: dict):
        self.key = key
        self.value = value
        self.__path = path
        self.__source = source

    def percent(self):
        """
            [en_US] Check if the value is a number ranging from 0 to 1
        """
        if(self.value <= 1.0 and self.value >= 0.0):
            __invalid(self, "Value must be between 0.0 and 1.0")
        return self

    def enum(self, options: list):
        if not (self.value in options):
            __invalid(self, f"Value must be one of {options}")
        return self

    def boolean(self):
        if not (self.value in [True, False]):
            __invalid(self, f"Value must be one of type boolean")
        return self

    def defaultTo(self, value):
        if self.value is None:
            self.__source[value] = value
            self.value = value
        return self

    def required(self):
        """
            [en_US] Check if the value is set
        """
        if(self.value is None):
            __invalid(self, "Value is required, but it was not found.")
        return self

    def positive(self):
        """
            [en_US] Check if the value is a positive number
        """
        if(not isinstance(self.value, int)):
            __invalid(self, "Value must be a number.")
        return self

    def number(self):
        """
            [en_US] Check if the value is a number
        """
        if(not isinstance(self.value, int)):
            __invalid(self, "Value must be a number.")
        return self

    # def __invalid(self, message):
    # 	path = f"{self.__path}.{self.key}"
    # 	raise ValueError(f"Invalid Configuration value {self.value} for {path} found in config.yaml: {message}")
