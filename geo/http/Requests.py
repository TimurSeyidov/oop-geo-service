import requests
from typing import Dict
from geo.abstract import HttpService


class Requests(HttpService):
    def get(self, url: str, params: Dict = None, headers: Dict = None) -> Exception | Dict:
        if not params:
            params = dict()
        if not headers:
            headers = dict()
        response = requests.get(url, params=params, headers=headers)
        if not response:
            raise Exception(response.status_code)
        return response.json()
