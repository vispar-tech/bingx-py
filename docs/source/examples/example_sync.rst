Synchronous Examples
====================

The synchronous client allows you to interact with the BingX API in a blocking manner.

Fetching Account Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from bingx_py import BingXHttpClient

   with BingXHttpClient(api_key="your_api_key", api_secret="your_api_secret") as client:
       account_data = client.spot.query_assets()
       print(account_data)

Placing a Spot Order
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from bingx_py import BingXHttpClient

   with BingXHttpClient(api_key="your_api_key", api_secret="your_api_secret") as client:
       order_response = client.spot.place_order(
           symbol="BTC-USDT",
           side="BUY",
           type="LIMIT",
           quantity=0.001,
           price=30000
       )
       print("Order placed:", order_response)

Fetching Market Data
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from bingx_py import BingXHttpClient

   with BingXHttpClient(api_key="your_api_key", api_secret="your_api_secret") as client:
       market_data = client.spot.get_spot_trading_symbols(symbol="BTC-USDT")
       print("Market data:", market_data)

Using `try-except-finally` block
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import asyncio
   from bingx_py import BingXHttpClient, exceptions

   def main():
       try:
           client.connect()
           client = BingXHttpClient(api_key="your_api_key", api_secret="your_api_secret")
           market_data = client.spot.get_spot_trading_symbols(symbol="BTC-USDT")
           print("Market data:", market_data)
       except exceptions.APIError as e:
           print("An error occurred:", e)
       finally:
            client.close()

   if __name__ == "__main__":
       main()
