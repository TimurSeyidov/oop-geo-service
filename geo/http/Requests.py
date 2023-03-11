import requests
from typing import Dict
from geo.abstract import HttpService


class Requests(HttpService):
    def get(self, url: str, params: Dict = None, headers: Dict = None, **opts) -> Exception | Dict:
        set_opts = dict()
        if params:
            set_opts['params'] = params
        if headers:
            set_opts['headers'] = headers
        timeout = opts.get('timeout')
        if timeout and type(timeout) == int:
            set_opts['timeout'] = timeout
        response = requests.get(url, **set_opts)
        if not response:
            raise Exception(f'{response.status_code}: {response.text}')
        return response.json()

    def post(self, url: str, params: Dict = None, headers: Dict = None, body: Dict = None, **opts) -> Exception | Dict:
        set_opts = dict()
        if params:
            set_opts['params'] = params
        if headers:
            set_opts['headers'] = headers
        if body:
            set_opts['data'] = body
        timeout = opts.get('timeout')
        if timeout and type(timeout) == int:
            set_opts['timeout'] = timeout
        response = requests.post(url, **set_opts)
        if not response:
            raise Exception(response.status_code)
        return response.json()
