from unittest.mock import patch
from market_data.alpaca_data_provider import AlpacaDataProvider
from dotenv import load_dotenv

from tests.mock_data.mock_stock_data import mock_historical_data

load_dotenv()


def test_get_historical_market_data():
    """Test the get_historical_market_data method of AlpacaDataProvider"""
    tickers = ["AAPL"]
    mock_data = mock_historical_data
    expected_dataframe = mock_historical_data.df
    with patch(
        "alpaca.data.StockHistoricalDataClient.get_stock_bars"
    ) as mock_get_stock_bars:
        mock_get_stock_bars.return_value = mock_data

        provider = AlpacaDataProvider()

        actual_result_df = provider.get_historical_market_data(tickers)

        mock_get_stock_bars.assert_called_once()
        assert not actual_result_df.empty
        assert list(actual_result_df.columns) == list(expected_dataframe.columns)
        assert (
            actual_result_df.loc["AAPL"]["vwap"].iloc[1]
            == expected_dataframe.loc["AAPL"]["vwap"].iloc[1]
        )
