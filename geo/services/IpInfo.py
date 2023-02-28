from geo import Ip, Point, Place
from geo.abstract import IpService, HttpService


class IpInfo(IpService):
    def __init__(self, token: str, http: HttpService):
        super().__init__(http)
        self.__token = token

    def get_info(self, ip: Ip) -> Exception | Place:
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
