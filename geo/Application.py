import os
from dotenv import load_dotenv
from typing import Any

from geo.helpers import IpServiceChain
from geo.services import IpInfo, Ip2Me, IpApi
from geo.http import Requests
from geo.components import FileCache
from geo import Ip, Place
from geo.abstract import HttpService


class Application:
    def __init__(self, env_file: str):
        load_dotenv(env_file)
        http = Requests()
        services = list()
        ip_info_token = self.get_param('ipinfo_token')
        if ip_info_token:
            services.append(IpInfo(token=ip_info_token, http=http))
        services.append(Ip2Me(http=http))
        services.append(IpApi(http=http))
        chain = IpServiceChain(http, *services)
        chain.cache = FileCache(folder='./cache', default_lifetime=10)
        self.__service = chain
        self.__http = http

    def get_ip_info(self, ip: Ip) -> Exception | Place:
        return self.__service.get_info(ip)

    @property
    def http(self) -> HttpService:
        return self.__http

    def run(self):
        pass

    @staticmethod
    def get_param(name: str, default: Any = None) -> Any:
        return os.environ.get(name, default)
