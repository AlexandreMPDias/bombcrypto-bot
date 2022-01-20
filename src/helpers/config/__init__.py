from src.helpers.config.root import ConfigRoot


class Config:
    def __init__(self, config) -> None:
        self.__root = ConfigRoot(config)

        self.values = self.__root.values
        self.thresholds = self.__root.thresholds
        self.time_intervals = self.__root.time_intervals

    def get(self, key: str):
        if key not in self.__root.values:
            raise Exception(f"Config: key [{key}] not found")
