from dataclasses import dataclass
from .Ip import Ip
from .Point import Point


@dataclass(frozen=True)
class Place:
    ip: Ip
    country: str | None
    region: str | None
    city: str | None
    zip: str | None
    point: Point

    def __repr__(self):
        return ', '.join(
            map(str, filter(bool, [
                self.zip,
                self.country,
                self.region,
                self.city,
                self.ip,
                self.point,
            ]))
        )
