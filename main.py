import os
from dotenv import load_dotenv
from geo import Ip
from geo.services import IpInfo
from geo.http import Requests

load_dotenv('./.env')

http = Requests()
service = IpInfo(token=os.getenv('ipinfo_token'), http=http)
point = service.get_info(Ip('8.8.8.8'))
print(point)
