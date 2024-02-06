import os
import pandas as pd
import logging
from alpaca.data import StockHistoricalDataClient
from alpaca.data import StockLatestQuoteRequest
from .data_provider import DataProvider


class AlpacaDataProvider(DataProvider):
    def __init__(self):
        self.ALPACA_API_KEY = os.environ.get("ALPACA_API_KEY")
        self.ALPACA_API_SECRET = os.environ.get("ALPACA_API_SECRET")
        self.ALPACA_BASE_URL = os.environ.get("ALPACA_BASE_URL")
        self.client = StockHistoricalDataClient(
            self.ALPACA_API_KEY, self.ALPACA_API_SECRET
        )

    def get_historical_market_data(self, ticker: list) -> pd.DataFrame:
        """Gets historical market data for given ticker and time period from Alpaca Markets"""
        market_data_df = pd.DataFrame()
        print(ticker)

        return market_data_df

    def get_current_ask_price(self, ticker: str) -> float:
        """Returns the current market price for a given ticker list \n
        ticker: stock ticker (ex: AAPL) \n returns current ask price"""

        if not ticker:
            logging.warning("No ticker provided")
            return

        request_params = StockLatestQuoteRequest(symbol_or_symbols=[ticker])
        latest_quote = self.client.get_stock_latest_quote(request_params)

        return latest_quote[ticker].ask_price

    def get_current_bid_price(self, ticker: str) -> float:
        """Returns the current market price for a given ticker list \n
        ticker: stock ticker (ex: AAPL) \n returns current bid price"""

        if not ticker:
            logging.warning("No ticker provided")
            return

        request_params = StockLatestQuoteRequest(symbol_or_symbols=[ticker])
        latest_quote = self.client.get_stock_latest_quote(request_params)

        return latest_quote[ticker].bid_price
