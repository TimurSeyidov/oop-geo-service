from geo import Ip, Place
from geo.abstract import IpService, HttpService


class IpServiceChain(IpService):
    def __init__(self, http: HttpService, *services: IpService):
        super().__init__(http)
        if not len(services):
            raise Exception('Please set one ore more services of ip')
        self.__services = services

    @staticmethod
    def __calculate_weight(place: Place) -> float:
        properties = ['country', 'region', 'city', 'zip', 'point']
        checked = 0
        for prop in properties:
            value = place.__getattribute__(prop)
            if value:
                checked += 1
        return checked / len(properties)

    def get_info(self, ip: Ip) -> Exception | Place | None:
        results = list()
        error = None
        for service in self.__services:
            try:
                place = service.get_info(ip)
                weight = self.__calculate_weight(place)
                print(service.__class__.__name__, weight)
                if weight == 1:
                    return place
                results.append((weight, place))
            except Exception as e:
                error = e
        if not results:
            if error:
                raise error
            else:
                return None
        item = max(results, key=lambda p: p[0])
        return item[1]