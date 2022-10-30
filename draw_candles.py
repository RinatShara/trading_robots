from tinkoff.invest import Client
from tokens import ro_token, sb_token
import pandas as pd
from datetime import datetime, timezone, timedelta
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 1500)
pd.set_option('display.width', 1000)


with Client(ro_token) as client:

	instruments = {}


	def convert_money(amount):
		return amount.units + amount.nano / 1e9


	def convert_time(time):
		time = time.replace(tzinfo=timezone.utc)
		tz = datetime.strptime('+0500', '%z').tzinfo
		time = time.astimezone(tz)
		return time


	def add_active(figi):
		instruments[figi] = [client.instruments.get_instrument_by(id_type=1, id=figi).instrument.name,
		                     client.instruments.get_instrument_by(id_type=1, id=figi).instrument.currency,
		                     client.instruments.get_instrument_by(id_type=1, id=figi).instrument.lot]


	def get_name(figi):
		if figi not in instruments.keys():
			add_active(figi)
		return instruments[figi][0]


	def get_currency(figi):
		if figi not in instruments.keys():
			add_active(figi)
		return instruments[figi][1]


	def get_lot(figi):
		if figi not in instruments.keys():
			add_active(figi)
		return instruments[figi][2]


	candles = client.market_data.get_candles(figi='BBG004730ZJ9',
	                                         from_=datetime(2022, 6, 24),
	                                         to=datetime(2022, 6, 25),
	                                         interval=1).candles

	df = pd.DataFrame([{'Название': get_name('BBG004730ZJ9'),
	                    'Валюта': get_currency('BBG004730ZJ9'),
	                    'Время': convert_time(item.time),
	                    'Цена открытия': convert_money(item.open),
	                    'Цена закрытия': convert_money(item.close),
	                    'Минимальное значение': convert_money(item.low),
	                    'Максимальное значение': convert_money(item.high)} for item in candles],
	                  index=[i for i in range(1, len(candles) + 1)])
	print(df)

	figure = plt.figure(figsize=(10, 7))
	ax = figure.add_subplot()
	ax.plot(df['Время'], df['Цена закрытия'])
	plt.show()
