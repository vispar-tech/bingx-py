Handling API Changes and Accessing Raw Data
===========================================

The BingX API may occasionally update its response structures, which can cause parsing errors in your code. To handle such cases gracefully, the client provides access to the raw response data via the `initial_data` parameter.

Accessing Raw Response Data
---------------------------

If a parsing error occurs due to changes in the API response structure, you can access the raw response data using the `initial_data` attribute. This attribute contains the original dictionary (`dict[str, Any]`) returned by the API before any parsing or validation.

Example:
--------

.. code-block:: python

   from python_bingx import BingXClient
   from python_bingx.exceptions import ConversationError

   client = BingXClient(api_key="your_api_key", api_secret="your_api_secret")

   try:
       response = client.spot.get_market_data(symbol="BTC-USDT")
   except ConversationError as e:
       print("Parsing failed due to changes in the API response structure.")
       print("Raw response data:", e.initial_data)  # Access the raw data
       raise  # Re-raise the exception if needed or process data as you need

Important Notes:
----------------

1. **Monitor API Changes**: Regularly check the BingX API documentation for updates to response structures.
2. **Fallback Mechanism**: Use `initial_data` as a fallback to handle unexpected changes in the API response.
3. **Logging**: Log the raw response data (`initial_data`) for debugging purposes when parsing fails.

Example with Logging:
---------------------

.. code-block:: python

   import logging
   from python_bingx import BingXClient
   from pydantic import ValidationError

   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)

   client = BingXClient(api_key="your_api_key", api_secret="your_api_secret")

   try:
       response = client.spot.get_market_data(symbol="BTC-USDT")
   except ValidationError as e:
       logger.error("Parsing failed due to changes in the API response structure.")
       logger.error("Raw response data: %s", e.initial_data)
       raise  # Re-raise the exception if needed or process data as you need
