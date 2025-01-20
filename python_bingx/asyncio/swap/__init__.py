"""Swap Perpetual API for BingX.

This module provides a comprehensive API for interacting with BingX's swap perpetual trading features.
It includes functionalities for account management, market data retrieval, and trade execution.

Classes:
    - `SwapPerpetualAPI`: Combines `AccountAPI`, `MarketAPI`, and `TradesAPI` to provide a unified interface
      for managing swap perpetual trading on BingX.
"""

from python_bingx.asyncio.swap.account import AccountAPI
from python_bingx.asyncio.swap.market import MarketAPI
from python_bingx.asyncio.swap.trades import TradesAPI


class SwapPerpetualAPI(AccountAPI, MarketAPI, TradesAPI):
    """API for managing swap perpetual on BingX.

    This class combines functionalities from `AccountAPI`, `MarketAPI`, and `TradesAPI` to provide
    a unified interface for managing swap perpetual trading, including account data, market data,
    and trade execution.
    """
