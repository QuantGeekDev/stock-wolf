from abc import ABC, abstractmethod
import pandas as pd


class DataProvider(ABC):
    @abstractmethod
    def get_historical_market_data(
        self,
        tickers: list,
    ) -> pd.DataFrame:
        """Gets historical market data for given ticker and time period"""

    @abstractmethod
    def get_current_ask_price(self, stock: str) -> float:
        """Returns the current market ask price for a given ticker"""

    @abstractmethod
    def get_current_bid_price(self, stock: str) -> float:
        """Returns the current market bid price for a given ticker"""
