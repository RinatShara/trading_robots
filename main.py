from tinkoff.invest import Client
from tokens import ro_token, sb_token
from datetime import datetime, timezone


with Client(ro_token) as client:
	instruments = {}
	currencies = {}


	def convert_money(amount):
		return amount.units + amount.nano / 1e9


	def convert_time(time):
		time = time.replace(tzinfo=timezone.utc)
		tz = datetime.strptime('+0500', '%z').tzinfo
		time = time.astimezone(tz)
		return time


	def find_active(figi):
		if figi not in instruments.keys():
			instruments[figi] = client.instruments.get_instrument_by(id_type=1, id=figi).instrument.name
		return instruments[figi]


	def get_currency(figi):
		if figi not in currencies.keys():
			currencies[figi] = client.instruments.get_instrument_by(id_type=1, id=figi).instrument.currency
		return currencies[figi]
