from tinkoff.invest import Client
from tokens import ro_token, sb_token
from datetime import datetime, timedelta

with Client(ro_token) as client:
	class MarketData:
		def get_candles(self):
			get_candles = client.market_data.get_candles(figi='BBG004730ZJ9',
			                                             from_=datetime(2022, 6, 23, 12, 0),
			                                             to=datetime(2022, 6, 23, 13, 40),
			                                             interval=1)
			print(get_candles)

		def get_last_prices(self):
			get_last_prices = client.market_data.get_last_prices(figi='BBG004730ZJ9')
			print(get_last_prices)

		def get_order_book(self):
			get_order_book = client.market_data.get_order_book(figi='BBG004730ZJ9', depth=20)
			print(get_order_book)

		def get_trading_status(self):
			get_trading_status = client.market_data.get_trading_status(figi='BBG004730ZJ9')
			print(get_trading_status)

		def get_last_trades(self):
			get_last_trades = client.market_data.get_last_trades(figi='BBG004730ZJ9',
			                                                     from_=datetime(2022, 6, 27, 12, 0),
			                                                     to=datetime(2022, 6, 27, 13, 0))
			print(get_last_trades)

	market_data = MarketData()

	# market_data.get_candles()  # Исторические свечи инструмента
	# market_data.get_last_prices()  # Последние цены по инструменту
	# market_data.get_order_book()  # Стакан инструмента
	# market_data.get_trading_status()  # Торговый статус инструмента
	# market_data.get_last_trades()  # Последние обезличенные сделки по инструменту на текущий торговый день


