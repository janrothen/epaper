import json
from enum import Enum

import requests


class Method(Enum):
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4


class HttpClient:
    def get(self, url: str) -> str:
        return self._perform(Method.GET, url)

    def post(self, url: str, json_data: dict | None = None) -> str:
        return self._perform(Method.POST, url, json_data)

    def put(self, url: str, json_data: dict | None = None) -> str:
        return self._perform(Method.PUT, url, json_data)

    def delete(self, url: str) -> str:
        return self._perform(Method.DELETE, url)

    def _perform(self, method: Method, url: str, json_data: dict | None = None) -> str:
        data = json.dumps(json_data) if json_data else None

        if method == Method.GET:
            r = requests.get(url)
        elif method == Method.POST:
            r = requests.post(url, data=data)
        elif method == Method.PUT:
            r = requests.put(url, data=data)
        elif method == Method.DELETE:
            r = requests.delete(url)

        if r.status_code not in (200, 201):
            raise ConnectionError(f"\nCode: {r.status_code}\nResult: {r.text}\nData: {data}")

        return r.text
