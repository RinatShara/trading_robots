from tinkoff.invest import Client, EditFavoritesRequestInstrument
from tokens import ro_token, sb_token
from datetime import datetime

with Client(ro_token) as client:
	class InstrumentsService:
		def trading_schedules(self):
			trading_schedules = client.instruments.trading_schedules(
				exchange='MOEX_PLUS',
				from_=datetime.now(),
				to=datetime(2022, 6, 30, 0, 0, 0))
			print(trading_schedules)

		def bond_by(self):
			bond_by = client.instruments.bond_by(id_type=1, id='BBG00QDTJQD2')
			print(bond_by)

		def bonds(self):
			bonds = client.instruments.bonds(instrument_status=1)
			print(bonds)

		def get_bond_coupons(self):
			get_bond_coupons = client.instruments.get_bond_coupons(
				figi='BBG00QDTJQD2',
				from_=datetime(2022, 1, 1, 0, 0, 0),
				to=datetime(2022, 6, 13, 0, 0, 0)
			)
			print(get_bond_coupons)

		def currency_by(self):
			currency_by = client.instruments.currency_by(id_type=1, id='BBG0013HGFT4')
			print(currency_by)

		def currencies(self):
			currencies = client.instruments.currencies(instrument_status=1)
			print(currencies)

		def etf_by(self):
			etf_by = client.instruments.etf_by(id_type=1, id='BBG333333333')
			print(etf_by)

		def etfs(self):
			etfs = client.instruments.etfs(instrument_status=1)
			print(etfs)

		def future_by(self):
			future_by = client.instruments.future_by(id_type=1, id='FUTGOLD03230')
			print(future_by)

		def futures(self):
			futures = client.instruments.futures(instrument_status=1)
			print(futures)

		def share_by(self):
			share_by = client.instruments.share_by(id_type=1, id='BBG009S39JX6')
			print(share_by)

		def shares(self):
			shares = client.instruments.shares(instrument_status=1)
			return shares
		
		def get_accrued_interests(self):
			get_accrued_interests = client.instruments.get_accrued_interests(
				figi='BBG00QDTJQD2',
				from_=datetime(2022, 1, 1, 0, 0, 0),
				to=datetime(2022, 6, 13, 0, 0, 0))
			print(get_accrued_interests)

		def get_futures_margin(self):
			get_futures_margin = client.instruments.get_futures_margin(figi='FUTGOLD03230')
			print(get_futures_margin)

		def get_instrument_by(self):
			get_instrument_by = client.instruments.get_instrument_by(id_type=1, id='BBG00QDTJQD2')
			print(get_instrument_by)

		def get_dividends(self):
			get_dividends = client.instruments.get_dividends(
				figi='BBG000BLWMN1',
				from_=datetime(2021, 1, 1, 0, 0, 0),
				to=datetime(2022, 6, 13, 0, 0, 0))
			print(get_dividends)

		def get_asset_by(self):
			get_asset_by = client.instruments.get_asset_by(id='9f083982-cf4c-418a-a0bf-8b82f16db42d')
			print(get_asset_by)

		def get_assets(self):
			get_assets = client.instruments.get_assets()
			print(str(get_assets)[:1001])

		def get_favorites(self):
			get_favorites = client.instruments.get_favorites()
			print(get_favorites)

		def edit_favorites(self):
			edit_favorites = client.instruments.edit_favorites(
				instruments=[EditFavoritesRequestInstrument(figi='BBG004730N88')],
				action_type=2)
			print(edit_favorites)

		def get_countries(self):
			get_countries = client.instruments.get_countries()
			print(get_countries)

		def find_instrument(self):
			find_instrument = client.instruments.find_instrument(query='Тинькофф')
			print(find_instrument)

		def get_brands_by(self):
			get_brands_by = client.instruments.get_brands_by(id='')
			print(get_brands_by)

		def get_brands(self):
			get_brands = client.instruments.get_brands()
			print(str(get_brands)[:1001])

	instrument_service = InstrumentsService()

	# instrument_service.trading_schedules()  # Расписание торгов торговых площадок
	# instrument_service.bond_by()  # Облигация по её идентификатору
	# instrument_service.bonds()  # Все облигации
	# instrument_service.get_bond_coupons()  # График выплат купонов по облигации
	# instrument_service.currency_by()  # Валюта по её идентификатору
	# instrument_service.currencies()  # Все валюты
	# instrument_service.etf_by()  # Инвестиционный фонд по его идентификатору
	# instrument_service.etfs()  # Все инвестиционные фонды
	# instrument_service.future_by()  # Фьючерс по его идентификатору
	# instrument_service.futures()  # Все фьючерсы
	# instrument_service.share_by()  # Акция по её идентификатору
	# instrument_service.shares()  # Все акции
	# instrument_service.get_accrued_interests()  # НКД каждый день в течение указанного периода
	# instrument_service.get_futures_margin()  # Размер гарантийного обеспечения по фьючерсам
	# instrument_service.get_instrument_by()  # Основная информация об инструменте
	# instrument_service.get_dividends()  # События выплаты дивидендов по инструменту
	# instrument_service.get_asset_by()  # Актив по его идентификатору
	# instrument_service.get_assets()  # Все активы
	# instrument_service.get_favorites()  # Все избранные инструменты
	# instrument_service.edit_favorites()  # Редактирование избранных инструментов
	# instrument_service.get_countries()  # Список стран
	# instrument_service.find_instrument()  # Поиск инструмента
	# instrument_service.get_brands_by()  # Бренд по его идентификатору
	# instrument_service.get_brands()  # Все бренды
