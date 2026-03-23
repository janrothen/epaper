import unittest
from pathlib import Path

from epaper.price.extractor import PriceExtractor
from epaper.price.mock import BitcoinPriceClientMock

FIXTURE = Path(__file__).parents[1] / "mock_data.json"


class TestPriceExtractorIntegration(unittest.TestCase):
    def setUp(self):
        self.data = BitcoinPriceClientMock(FIXTURE).retrieve_data()

    def test_format_usd_price(self):
        extractor = PriceExtractor("USD", "$")
        result = extractor.formatted_price_from_data(self.data)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("$"))

    def test_format_chf_price(self):
        extractor = PriceExtractor("CHF", "CHF")
        result = extractor.formatted_price_from_data(self.data)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("CHF"))

    def test_missing_data_returns_na(self):
        extractor = PriceExtractor("USD", "$")
        self.assertEqual(extractor.formatted_price_from_data(None), "N/A")
        self.assertEqual(extractor.formatted_price_from_data({}), "N/A")


if __name__ == "__main__":
    unittest.main()
