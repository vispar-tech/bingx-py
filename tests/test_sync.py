import logging
import os
import unittest

from dotenv import load_dotenv

from bingx_py import BingXClient, exceptions

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class TestSyncBingxClient(unittest.TestCase):
    def setUp(self) -> None:
        self.client = BingXClient(
            api_key=os.getenv("API_KEY", ""),
            api_secret=os.getenv("API_SECRET", ""),
            demo_trading=False,
        )

    def test_try_except_block(self) -> None:
        try:
            self.client.connect()
            response = self.client.spot.query_assets()
            print("Assets:", response)
            self.assertEqual(response.code, 0)
        except exceptions.APIError as e:
            print("An error occurred:", e)
        finally:
           self.client.close()

    def test_context(self) -> None:
        with self.client:
            response = self.client.spot.query_assets()
            print("Assets:", response)
            self.assertEqual(response.code, 0)
