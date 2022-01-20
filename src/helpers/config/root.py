from src.helpers.config.thresholds import ConfigThresholds
from src.helpers.config.time_intervals import ConfigTimeIntervals


class ConfigRoot:
    def __init__(self, config) -> None:
        self.values = dict(config)
        print(self.values, type(self.values))
        self.thresholds = ConfigThresholds(self.values)
        self.time_intervals = ConfigTimeIntervals(self.values)
