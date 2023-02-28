from geo import Ip, Place
from .HttpService import HttpService


class IpService:
    def __init__(self, http: HttpService):
        self.http = http

    def get_info(self, ip: Ip) -> Exception | Place:
        pass
