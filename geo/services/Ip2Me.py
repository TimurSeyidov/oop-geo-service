from geo import Ip, Point, Place
from geo.abstract import IpService


class Ip2Me(IpService):
    def get_info(self, ip: Ip) -> Exception | Place:
        data = self.http.get('https://api.2ip.me/geo.json', params={'ip': ip.value})
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
