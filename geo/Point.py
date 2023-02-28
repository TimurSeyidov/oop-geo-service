from math import pi, sin, cos, sqrt, pow, atan2


class Point:
    def __init__(self, lat: float, lng: float):
        self.__lat = lat
        self.__lng = lng

    @property
    def lat(self):
        return self.__lat

    @property
    def lng(self):
        return self.__lng

    def __repr__(self):
        return f'{self.__class__.__name__}({self.lat}, {self.lng})'

    def __sub__(self, point) -> float:
        RAD = 6372795
        lat1 = self.lat * pi / 180
        lat2 = point.lat * pi / 180
        lng1 = self.lng * pi / 180
        lng2 = point.lng * pi / 180
        c1 = cos(lat1)
        c2 = cos(lat2)
        s1 = sin(lat1)
        s2 = sin(lat2)
        delta = lng2 - lng1
        cdelta = cos(delta)
        sdelta = sin(delta)
        y = sqrt(pow(c2 * sdelta, 2) + pow(c1 * s2 - s1 * c2 * cdelta, 2))
        x = s1 * s2 + c1 * c2 * cdelta
        return atan2(y, x) * RAD
