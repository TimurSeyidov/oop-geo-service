from typing import Any
from time import time
import os, json
from os import path
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

    def __call__(self, *args, **kwargs):
        return {
            'expired': self.expired,
            'data': self.data
        }


class FileCache(Cache):
    def __init__(self, folder: str, default_lifetime: int = 60):
        super().__init__(default_lifetime)
        folder = path.abspath(folder)
        if not path.exists(folder) or not path.isdir(folder):
            os.makedirs(folder, 0o755)
        self.__folder = folder

    def get(self, key: str) -> str | None:
        cache_file = path.join(
            self.__folder,
            f'{key}.dat'
        )
        if not path.exists(cache_file) or not path.isfile(cache_file):
            return None
        with open(cache_file, 'r') as read_file:
            item = json.load(read_file)
            data = item.get('data')
            expired = item.get('expired')
            if not data or CacheItem.get_time() > expired:
                os.remove(cache_file)
                return None
            return data

    def set(self, key: str, value: str, lifetime: int = None) -> None:
        if not lifetime:
            lifetime = self.lifetime
        cache_file = path.join(
            self.__folder,
            f'{key}.dat'
        )
        item = CacheItem(
            data=value,
            lifetime=lifetime
        )
        with open(cache_file, 'w') as write_file:
            json.dump(item(), write_file)

