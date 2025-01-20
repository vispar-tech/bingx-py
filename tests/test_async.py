import logging
import os
import unittest

from dotenv import load_dotenv

from python_bingx import BingXAsyncClient, exceptions

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class TestAsyncBingxClient(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.client = BingXAsyncClient(
            api_key=os.getenv("API_KEY", ""),
            api_secret=os.getenv("API_SECRET", ""),
            demo_trading=False,
        )

    async def test_get_account(self) -> None:
        try:
            await self.client.connect_async()
            response = await self.client.spot.query_assets()
            print("Assets:", response)
            self.assertEqual(response.code, 0)
        except exceptions.APIError as e:
            print("An error occurred:", e)
        finally:
           await self.client.close_async()



    async def test_context(self) -> None:
        async with self.client:
            response = await self.client.spot.query_assets()
            print("Assets:", response)
            self.assertEqual(response.code, 0)
