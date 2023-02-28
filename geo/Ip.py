from ipaddress import ip_address, IPv4Address, IPv6Address


class Ip:
    def __init__(self, value: str):
        value = value.strip()
        if not value:
            raise ValueError('Empty IP string')
        try:
            self.__ip = ip_address(value)
        except:
            raise ValueError('Invalid IP value ' + value)

    @property
    def value(self) -> str:
        return self.__ip.__str__()

    @property
    def is_ip_v4(self) -> bool:
        return int(self.__ip.version) == 4

    @property
    def is_ip_v6(self) -> bool:
        return int(self.__ip.version) == 6

    def __repr__(self):
        return f'Ip({self.value})'
