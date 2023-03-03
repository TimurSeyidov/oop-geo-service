from typing import Any


class Cache:
    def __init__(self, default_lifetime: int = 60):
        self.__default_lifetime = default_lifetime

    @property
    def lifetime(self) -> int:
        return self.__default_lifetime

    def get(self, key: str) -> Any:
        pass

    def set(self, key: str, value: Any, lifetime: int = None) -> None:
        pass
