from typing import Dict

from geo import Ip, Point, Place
from geo.abstract import IpService, HttpService


class IpInfo(IpService):
    __cache_key__: str = 'ipinfo_'
    __cache_expired__: int = 3600

    def __init__(self, token: str, http: HttpService):
        super().__init__(http)
        self.__token = token

    @property
    def cache_key(self) -> str:
        return self.__cache_key__

    @property
    def cache_expired(self) -> int:
        return self.__cache_expired__

    def get_remote_data(self, ip: Ip) -> Exception | Dict:
        url = f'https://ipinfo.io/{ip.value}'
        data = self.http.get(
            url=url,
            params={
                'token': self.__token
            },
            headers={
                'Content-Type': 'application/json'
            }
        )
        return data

    def convert(self, ip: Ip, data: Dict) -> Place:
        lat, lng = data.get('loc', '').split(',')
        return Place(
            ip=ip,
            country=data.get('country'),
            region=data.get('region'),
            city=data.get('city'),
            zip=data.get('postal'),
            point=Point(
                lat=float(lat),
                lng=float(lng),
            )
        )
