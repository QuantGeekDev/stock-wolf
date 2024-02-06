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

print(data_provider.get_current_ask_price(ticker=tickers[0]))
