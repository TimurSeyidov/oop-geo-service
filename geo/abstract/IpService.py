from typing import Dict
from geo import Ip, Place
from geo.abstract import Cache
from .HttpService import HttpService


class IpService:
    def __init__(self, http: HttpService):
        self.__http = http
        self.__cache = None

    @property
    def http(self) -> HttpService:
        return self.__http

    @http.setter
    def http(self, value: HttpService):
        self.__http = value

    @property
    def cache(self) -> Cache:
        return self.__cache

    @cache.setter
    def cache(self, value: Cache):
        self.__cache = value

    def get_remote_data(self, ip: Ip) -> Exception | Dict:
        pass

    def convert(self, ip: Ip, data: Dict) -> Place:
        pass

    @property
    def cache_key(self) -> str:
        return '_'

    @property
    def cache_expired(self) -> int:
        return 0

    def get_info(self, ip: Ip) -> Exception | Place | None:
        data = None
        cache_key = None
        if self.cache:
            cache_key = self.cache_key + ip.value
            data = self.cache.get(cache_key)
        if not data:
            data = self.get_remote_data(ip)
            if cache_key:
                self.cache.set(cache_key, data, self.cache_expired)
        return self.convert(ip, data)
