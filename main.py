import logging
from dotenv import load_dotenv
from market_data.alpaca_data_provider import AlpacaDataProvider

load_dotenv()
logging.basicConfig()
logging.root.setLevel(logging.NOTSET)

logging.info("Starting StockWolf-Mini")

data_provider = AlpacaDataProvider()

tickers = ["GLD", "AAPL", "GOOGL"]
empty_symbols = []

market_data = data_provider.get_historical_market_data(tickers)
apple_market_data = market_data.loc["AAPL"]
print(apple_market_data)
