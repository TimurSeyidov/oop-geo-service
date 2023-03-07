from typing import Dict
from geo import Ip, Point, Place
from geo.abstract import IpService


class IpApi(IpService):
    __cache_key__: str = 'ipapi_'
    __cache_expired__: int = 3600

    @property
    def cache_key(self) -> str:
        return self.__cache_key__

    @property
    def cache_expired(self) -> int:
        return self.__cache_expired__

    def get_remote_data(self, ip: Ip) -> Exception | Dict:
        data = self.http.get(
            url=f'http://ip-api.com/json/{ip.value}',
            params={
                'lang': 'ru',
                'fields': ','.join([
                    'status',
                    'message',
                    'country',
                    'regionName',
                    'city',
                    'zip',
                    'lat',
                    'lon'
                ])
            })
        if data.get('status') != 'success':
            raise Exception(data.get('message'))
        return data

    def convert(self, ip: Ip, data: Dict) -> Place:
        return Place(
            ip=ip,
            country=data.get('country'),
            region=data.get('regionName'),
            city=data.get('city'),
            zip=data.get('zip'),
            point=Point(
                lat=float(data.get('lat')),
                lng=float(data.get('lon')),
            )
        )
