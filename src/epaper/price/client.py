import json
import logging

from epaper.config import config
from epaper.http_client import HttpClient


class BitcoinPriceClient:
    def retrieve_data(self) -> dict | None:
        endpoint = config()["bitcoin"]["price"]["service_endpoint"]
        try:
            result = HttpClient().get(endpoint)
            if result:
                return json.loads(result)
        except ConnectionError as e:
            logging.error(str(e))
        return None
