from geo import Ip, Point, Place
from geo.abstract import IpService


class IpApi(IpService):
    def get_info(self, ip: Ip) -> Exception | Place | None:
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
