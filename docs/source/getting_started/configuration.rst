Configuration
=============

The Python BingX API Client supports flexible caching and global configuration.

Caching
-------

The client supports both synchronous and asynchronous caching, including in-memory and Redis-based caches.

Using an In-Memory Cache
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from bingx_py import BingXHttpClient
   from bingx_py.caching import SyncMemoryCache

   cache = SyncMemoryCache()
   client = BingXHttpClient(
       api_key="your_api_key",
       api_secret="your_api_secret",
       cache=cache,
       default_cache_ttl=300  # Cache responses for 5 minutes
   )

Using Redis Cache
^^^^^^^^^^^^^^^^^

.. code-block:: python

   from bingx_py import BingXHttpClient
   from bingx_py.caching import SyncRedisCache

   cache = SyncRedisCache(host="localhost", port=6379, db=0)
   client = BingXHttpClient(
       api_key="your_api_key",
       api_secret="your_api_secret",
       cache=cache,
   )

Global Configuration
--------------------

You can configure caching globally using the `cache_config` module:

.. code-block:: python

   from bingx_py import cache_config

   # Set a synchronous Redis cache globally
   cache_config.set_cache("sync-redis", host="localhost", port=6379, db=0)

   # Enable unsafe caching for non-GET requests
   cache_config.enable_unsafe_cache()

   # Disable unsafe caching
   cache_config.disable_unsafe_cache()
