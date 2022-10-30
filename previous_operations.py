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
		time = time.replace(microsecond=0, tzinfo=timezone.utc)
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


	operations = client.operations.get_operations(account_id='2006363341',
	                                              from_=datetime.now() - timedelta(days=365 * 5),
	                                              to=datetime.now()).operations
	df = pd.DataFrame([{'Дата': convert_time(item.date),
	                    'Описание операции': item.type,
	                    'Название': get_name(item.figi) if item.figi else '-',
	                    'Тип': item.instrument_type,
	                    'Валюта': item.currency,
	                    'Стоимость актива': convert_money(item.price),
	                    'Количество': item.quantity,
	                    'Стоимость операции': convert_money(item.payment)} for item in operations],
	                  index=[i for i in range(len(operations), 0, -1)])
	print(df.sort_values('Дата', axis=0))
