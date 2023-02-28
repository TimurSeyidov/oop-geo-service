import unittest
from geo import Point


class TestPoint(unittest.TestCase):
    def test_create(self):
        lat = 12.234
        lng = 23.46
        point = Point(lat, lng)
        self.assertEqual(point.lat, lat, 'Широта задана неверно')
        self.assertEqual(point.lng, lng, 'Долгота задана неверно')

    def test_distance(self):
        a = Point(55.75059, 37.61777)
        b = Point(50.44952, 30.52537)
        need = 755510
        self.assertTrue(755000 <= int(a - b) <= need)


if __name__ == '__main__':
    unittest.main()
