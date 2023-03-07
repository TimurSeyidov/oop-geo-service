import os
from dotenv import load_dotenv

from geo.helpers import IpServiceChain
from geo.services import IpInfo, Ip2Me, IpApi
from geo.http import Requests
from geo.components import FileCache
from geo import Ip, Place


class Application:
    def __init__(self, env_file: str):
        load_dotenv(env_file)
        http = Requests()
        ip_info = IpInfo(token=os.getenv('ipinfo_token'), http=http)
        ip_2me = Ip2Me(http=http)
        ip_api = IpApi(http=http)
        chain = IpServiceChain(http, ip_info, ip_api, ip_2me)
        chain.cache = FileCache(folder='./cache', default_lifetime=10)
        self.__service = chain

    def get_ip_info(self, ip: Ip) -> Exception | Place:
        return self.__service.get_info(ip)
    
    def run(self):
        pass
