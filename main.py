import os
from dotenv import load_dotenv
from time import sleep
from geo import Ip, Point, Place
from geo.abstract import IpService
from geo.services import IpInfo, Ip2Me, IpApi
from geo.http import Requests
from geo.helpers import IpServiceChain
from geo.components import FileCache

load_dotenv('./.env')

cache = FileCache(folder='./cache', default_lifetime=10)
cache.set('abs', 'Hello world')
for i in range(10):
    print(i * 2, 'sec', cache.get('abs'))
    sleep(2)


# class FakeService(IpService):
#     def get_info(self, ip: Ip) -> Exception | Place:
#         return Place(
#             ip=ip,
#             country='США',
#             point=Point(123, 123),
#             zip=None,
#             city=None,
#             region=None
#         )


# http = Requests()
# ip_info = IpInfo(token=os.getenv('ipinfo_token'), http=http)
# ip_2me = Ip2Me(http=http)
# ip_api = IpApi(http=http)
# fake = FakeService(http=http)
# chain = IpServiceChain(http, fake, ip_api, ip_info, ip_2me)
#
# point = chain.get_info(Ip('8.8.8.8'))
# print(point)
