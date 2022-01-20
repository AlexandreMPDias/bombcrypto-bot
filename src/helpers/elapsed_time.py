import time
from src.helpers.add_randomness import add_randomness


class ElapsedTime:
    def __init__(self, timeouts: dict, multiplier: int = 60):
        self.__last = {}
        self.__multiplier = multiplier
        self.__timeouts = timeouts
        for key, _ in timeouts.items():
            self.__last[key] = 0

    def checkTimeout(self, key: str, randomness=True):
        now = time.time()
        if key not in self.__last:
            raise Exception(f"ElapsedTime.checkTimeout: unknown [{key}]")

        base_timeout = self.__timeouts[key] * self.__multiplier
        timeout = add_randomness(base_timeout) if randomness else base_timeout

        if now - self.__last[key] > timeout:
            self.__last[key] = now
            return True
        return False

    def last(self, key: str):
        if key not in self.__last:
            raise Exception(f"ElapsedTime.last: unknown [{key}]")
        return self.__last[key]
