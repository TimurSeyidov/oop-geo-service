import unittest
from typing import Dict
from geo import Ip, Place
from geo.abstract import HttpService
from geo.services import Ip2Me


class FakeHttpService(HttpService):
    def __init__(self, data: Dict):
        self.data = data

    def get(self, url: str, params: Dict = None, headers: Dict = None) -> Exception | Dict:
        return self.data


class TestIpService(unittest.TestCase):
    def __test_place(self, place: Place):
        self.assertEqual(place.country, 'США')
        self.assertEqual(place.region, 'Калифорния')
        self.assertEqual(place.city, 'Маунтин Вью')
        self.assertEqual(place.zip, '94043')
        self.assertEqual(place.ip.value, '8.8.8.8')
        self.assertEqual(place.point.lat, 37.405992)
        self.assertEqual(place.point.lng, -122.078515)

    def test_ip2me(self):
        data = {
            'country_rus': 'США',
            'region_rus': 'Калифорния',
            'city': 'Маунтин Вью',
            'latitude': '37.405992',
            'longitude': '-122.078515',
            'zip_code': '94043',
        }
        http = FakeHttpService(data)
        service = Ip2Me(http)
        self.__test_place(service.get_info(Ip('8.8.8.8')))


if __name__ == '__main__':
    unittest.main()
