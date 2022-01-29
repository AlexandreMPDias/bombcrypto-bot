from src.helpers.debug import log, Paint


class ConfigValidationRuleConstructor:
    def __init__(self, key: str,  path: str, source: dict):
        self.key = key
        self.__path = path
        self.__source = source
        self.value = self.__source[self.key]

    def raiseInvalid(self, message: str):
        path = f"{self.__path}.{self.key}"

        pValue = Paint.red(f"[ {self.value} ]")
        pPath = Paint.yellow(f"[ {path} ]")

        log.error(
            f"Invalid Configuration value {pValue} for {pPath} found in config.yaml\n")
        print(Paint.red(f"{message}\n"))

        raise ValueError(
            f"Invalid Configuration value {self.value} for {path} found in config.yaml: {message}")

    def castValue(self, next):
        self.value = next
        self.__source[self.key] = self.value
