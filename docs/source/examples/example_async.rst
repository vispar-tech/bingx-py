Asynchronous Examples
=====================

The asynchronous client allows you to interact with the BingX API in a non-blocking manner.

Fetching Account Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import asyncio
   from python_bingx import BingXHttpClient

   async def main():
       async with BingXHttpClient(api_key="your_api_key", api_secret="your_api_secret") as client:
           account_data = await client.spot.query_assets()
           print(account_data)

   asyncio.run(main())

Placing a Spot Order
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import asyncio
   from python_bingx import BingXHttpClient

   async def main():
       async with BingXHttpClient(api_key="your_api_key", api_secret="your_api_secret") as client:
           order_response = await client.spot.place_order(
               symbol="BTC-USDT",
               side="BUY",
               type="LIMIT",
               quantity=0.001,
               price=30000
           )
           print("Order placed:", order_response)

   asyncio.run(main())

Fetching Market Data
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import asyncio
   from python_bingx import BingXHttpClient

   async def main():
       async with BingXHttpClient(api_key="your_api_key", api_secret="your_api_secret") as client:
           market_data = await client.spot.get_spot_trading_symbols(symbol="BTC-USDT")
           print("Market data:", market_data)

   asyncio.run(main())

Using `try-except-finally` block
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import asyncio
   from python_bingx import BingXHttpClient, exceptions

   async def main():
       client = None
       try:
           await client.connect_async()
           client = BingXHttpClient(api_key="your_api_key", api_secret="your_api_secret")
           market_data = await client.spot.get_spot_trading_symbols(symbol="BTC-USDT")
           print("Market data:", market_data)
       except exceptions.APIError as e:
           print("An error occurred:", e)
       finally:
           await client.close_async()

   asyncio.run(main())
