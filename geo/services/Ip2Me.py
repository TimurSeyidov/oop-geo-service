from typing import Dict
from geo import Ip, Point, Place
from geo.abstract import IpService


class Ip2Me(IpService):
    __cache_key__: str = '2ip_me_'
    __cache_expired__: int = 3600

    @property
    def cache_key(self) -> str:
        return self.__cache_key__

    @property
    def cache_expired(self) -> int:
        return self.__cache_expired__

    def get_remote_data(self, ip: Ip) -> Exception | Dict:
        return self.http.get('https://api.2ip.me/geo.json', params={'ip': ip.value}, timeout=3)

    def convert(self, ip: Ip, data: Dict) -> Place:
        return Place(
            ip=ip,
            country=data.get('country_rus'),
            region=data.get('region_rus'),
            city=data.get('city'),
            zip=data.get('zip_code'),
            point=Point(
                lat=float(data.get('latitude')),
                lng=float(data.get('longitude')),
            )
        )


