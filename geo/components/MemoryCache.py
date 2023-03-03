from typing import Any
from time import time
from geo.abstract import Cache


class CacheItem:
    def __init__(self, lifetime: int, data: Any):
        self.__expired = self.get_time(lifetime)
        self.__data = data

    @staticmethod
    def get_time(offset: int = 0):
        return int(time() + offset)

    @property
    def expired(self) -> int:
        return self.__expired

    @property
    def data(self) -> Any:
        return self.__data

    @property
    def is_actual(self) -> bool:
        return self.expired >= self.get_time()


class MemoryCache(Cache):
    def __init__(self, default_lifetime: int = 60):
        super().__init__(default_lifetime)
        self.__storage = dict()

    def get(self, key: str) -> Any:
        item = self.__storage.get(key)
        if not item or not item.is_actual:
            return None
        return item.data

    def set(self, key: str, value: Any, lifetime: int = None) -> None:
        if not lifetime:
            lifetime = self.lifetime
        self.__storage[key] = CacheItem(
            data=value,
            lifetime=lifetime
        )

