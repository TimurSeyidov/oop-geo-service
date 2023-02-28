import unittest
from geo import Place, Ip, Point


class TestPlace(unittest.TestCase):
    @staticmethod
    def __get_place():
        return Place(
            ip=Ip('8.8.8.8'),
            country='США',
            region='Калифорния',
            city='Маунтин Вью',
            zip='94043',
            point=Point(37.405992, -122.078515)
        )

    def test_success(self):
        place = self.__get_place()
        self.assertEqual(place.country, 'США')
        self.assertEqual(place.region, 'Калифорния')
        self.assertEqual(place.city, 'Маунтин Вью')
        self.assertEqual(place.zip, '94043')
        self.assertEqual(place.ip.value, '8.8.8.8')
        self.assertEqual(place.point.lat, 37.405992)
        self.assertEqual(place.point.lng, -122.078515)

    def test_failed(self):
        place = self.__get_place()
        self.assertNotEqual(place.country, 'Россия')


if __name__ == '__main__':
    unittest.main()
