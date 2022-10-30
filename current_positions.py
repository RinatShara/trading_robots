from tinkoff.invest import Client
from tokens import ro_token, sb_token
import pandas as pd
from datetime import datetime, timezone


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
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


	positions = client.operations.get_portfolio(account_id='2006363341').positions
	df = pd.DataFrame([{'Название': get_name(item.figi),
	                    'Тип': item.instrument_type,
	                    'Валюта': item.current_price.currency,
	                    'Количество': convert_money(item.quantity),
	                    'Средняя цена покупки': convert_money(item.average_position_price_fifo),
	                    'Текущая цена': convert_money(item.current_price),
	                    'Потрачено': convert_money(item.average_position_price_fifo) * convert_money(item.quantity),
	                    'Получено бы': convert_money(item.current_price) * convert_money(item.quantity),
	                    } for item in positions[:101]], index=[i for i in range(1, len(positions) + 1)])
	df['Потрачено'] = df['Количество'] * df['Средняя цена покупки']
	df['Получено бы'] = df['Количество'] * df['Текущая цена']
	df['Текущая доходность'] = df['Получено бы'] - df['Потрачено']
	df['Комиссия'] = df['Получено бы'] * 0.003
	print(df)
