from tinkoff.invest import Client
from tokens import ro_token, sb_token

with Client(ro_token) as client:
	class OrdersService:
		def post_order(self):
			post_order = client.orders.post_order(
				figi='',
				quantity='',
				price='',
				direction='',
				account_id='',
				order_type='',
				order_id='')
			print(post_order)

		def cancel_order(self):
			cancel_order = client.orders.cancel_order(account_id='2006363341', order_id='')
			print(cancel_order)

		def get_order_state(self):
			get_order_state = client.orders.get_order_state(account_id='2006363341', order_id='31609417314')
			print(get_order_state)

		def get_orders(self):
			get_orders = client.orders.get_orders(account_id='2006363341')
			print(get_orders)

	orders_service = OrdersService()

	# orders_service.post_order()  # Выставление торгового поручения
	# orders_service.cancel_order()  # Отмена торгового поручения
	# orders_service.get_order_state()  # Статус торгового поручения
	# orders_service.get_orders()  # Список активных торговых поручений
