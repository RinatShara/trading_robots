from tinkoff.invest import Client
from tokens import ro_token, sb_token
from datetime import datetime, timedelta

with Client(ro_token) as client:
	class StopOrders:
		def post_stop_order(self):
			post_stop_order = client.stop_orders.post_stop_order(
				figi='',
				quantity='',
				price='',
				stop_price='',
				direction='',
				account_id='',
				expiration_type='',
				stop_order_type='',
				expire_date=''
			)
			print(post_stop_order)

		def get_stop_orders(self):
			get_stop_orders = client.stop_orders.get_stop_orders(account_id='2006363341')
			print(get_stop_orders)

		def cancel_stop_order(self):
			cancel_stop_order = client.stop_orders.cancel_stop_order(account_id='2006363341', stop_order_id='')
			print(cancel_stop_order)

	stop_orders = StopOrders()

	# stop_orders.post_stop_order()  # Выставление стоп-заявки
	# stop_orders.get_stop_orders()  # Список активных стоп-заявок по счёту
	# stop_orders.cancel_stop_order()  # Отмена стоп-заявки
