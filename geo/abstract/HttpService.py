from typing import Dict


class HttpService:
    def get(self, url: str, params: Dict = None, headers: Dict = None, **opts) -> Exception | Dict:
        pass

    def post(self, url, params: Dict = None, headers: Dict = None, body: Dict = None, **opts) -> Exception | Dict:
        pass
