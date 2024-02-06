import os
import pandas as pd
import logging
import datetime
from alpaca.data import StockHistoricalDataClient
from alpaca.data import StockLatestQuoteRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from .data_provider import DataProvider


class AlpacaDataProvider(DataProvider):
    def __init__(self):
        logging.debug("Initializing AlpacaDataProvider")

        self.ALPACA_API_KEY = os.environ.get("ALPACA_API_KEY")
        self.ALPACA_API_SECRET = os.environ.get("ALPACA_API_SECRET")
        self.ALPACA_BASE_URL = os.environ.get("ALPACA_BASE_URL")
        self.DEFAULT_TIMEFRAME = os.environ.get("DEFAULT_TIMEFRAME")
        self.timeframe = self.get_timeframe()
        self.client = StockHistoricalDataClient(
            self.ALPACA_API_KEY, self.ALPACA_API_SECRET
        )

    def get_historical_market_data(self, tickers: list) -> pd.DataFrame:
        """Gets historical market data for given ticker and time period from Alpaca Markets"""
        start_date = self.get_start_date()
        bars_request_params = StockBarsRequest(
            symbol_or_symbols=tickers, timeframe=self.timeframe, start=start_date
        )
        market_data = self.client.get_stock_bars(bars_request_params)
        market_data_df = market_data.df
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

    def get_timeframe(self):
        """Returns the timeframe object from a string \n
        Valid inputs: 1Month, 1Day, 1Hour, 1Minute"""
        if self.DEFAULT_TIMEFRAME is None:
            logging.error("DEFAULT_TIMEFRAME not set!")
            return
        elif self.DEFAULT_TIMEFRAME == "1Month":
            return TimeFrame.Month

        elif self.DEFAULT_TIMEFRAME == "1Day":
            return TimeFrame.Day

        elif self.DEFAULT_TIMEFRAME == "1Hour":
            return TimeFrame.Hour

        elif self.DEFAULT_TIMEFRAME == "1Minute":
            return TimeFrame.Minute

        logging.error(
            "Timeframe is not compatible, please select a valid timeframe  (ex: 1Month, 1Day"
        )
        return

    def get_start_date(self, periods=30):
        """Returns the start date based on periods selected \n Defaults to 30 periods"""
        if self.timeframe.value == "1Day":
            start_date = datetime.datetime.now() - datetime.timedelta(days=periods)
            return start_date
        elif self.timeframe.value == "1Hour":
            start_date = datetime.datetime.now() - datetime.timedelta(hours=periods)
            return start_date
        elif self.timeframe.value == "1Min":
            start_date = datetime.datetime.now() - datetime.timedelta(minutes=periods)
            return start_date
        elif self.timeframe.value == "1Month":
            start_date = datetime.datetime.now() - datetime.timedelta(
                days=(periods * 30)
            )
            return start_date
