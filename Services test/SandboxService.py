from tinkoff.invest import Client, MoneyValue, Quotation
from tokens import ro_token, sb_token
from datetime import datetime, timedelta

with Client(sb_token) as client:
	class Sandbox:
		def open_sandbox_account(self):
			open_sandbox_account = client.sandbox.open_sandbox_account()
			print(open_sandbox_account)

		def get_sandbox_accounts(self):
			get_sandbox_accounts = client.sandbox.get_sandbox_accounts()
			print(get_sandbox_accounts)

		def close_sandbox_account(self):
			close_sandbox_account = client.sandbox.close_sandbox_account(account_id='ebb8b629-1ad7-4f1d-a93f-09fb93e32487')
			print(close_sandbox_account)

		def sandbox_pay_in(self):
			sandbox_pay_in = client.sandbox.sandbox_pay_in(account_id='ebb8b629-1ad7-4f1d-a93f-09fb93e32487',
			                                               amount=MoneyValue(currency='rub', units=1000, nano=000000000))
			print(sandbox_pay_in)

		def get_sandbox_operations(self):
			get_sandbox_operations = client.sandbox.get_sandbox_operations(
				account_id='ebb8b629-1ad7-4f1d-a93f-09fb93e32487',
				from_=datetime.now() - timedelta(days=365 * 5),
				to=datetime.now(),
				# state=1,
				# figi='BBG000BBQCY0'
			)
			print(get_sandbox_operations)

		def get_sandbox_portfolio(self):
			get_sandbox_portfolio = client.sandbox.get_sandbox_portfolio(account_id='ebb8b629-1ad7-4f1d-a93f-09fb93e32487')
			print(get_sandbox_portfolio)

		def get_sandbox_positions(self):
			get_sandbox_positions = client.sandbox.get_sandbox_positions(account_id='ebb8b629-1ad7-4f1d-a93f-09fb93e32487')
			print(get_sandbox_positions)

		def post_sandbox_order(self):
			post_sandbox_order = client.sandbox.post_sandbox_order(
				figi='BBG004730N88',
				quantity=1,
				# price=Quotation(units=1, nano=0),
				direction=2,
				account_id='ebb8b629-1ad7-4f1d-a93f-09fb93e32487',
				order_type=2,
				order_id=datetime.now().strftime('%Y-%m-%dT %H:%M:%S')
			)
			print(post_sandbox_order)

		def get_sandbox_orders(self):
			get_sandbox_orders = client.sandbox.get_sandbox_orders(account_id='ebb8b629-1ad7-4f1d-a93f-09fb93e32487')
			print(get_sandbox_orders)

		def get_sandbox_order_state(self):
			get_sandbox_order_state = client.sandbox.get_sandbox_order_state(
				account_id='ebb8b629-1ad7-4f1d-a93f-09fb93e32487',
				order_id='f5e21746-9b66-4a81-bb3d-e036651608d4'
			)
			print(get_sandbox_order_state)

		def cancel_sandbox_order(self):
			cancel_sandbox_order = client.sandbox.cancel_sandbox_order(
				account_id='ebb8b629-1ad7-4f1d-a93f-09fb93e32487',
				order_id='daf1d31e-b0be-44b4-a313-72b6e7dd0bfe'
			)
			print(cancel_sandbox_order)

	sandbox = Sandbox()

	# sandbox.open_sandbox_account()  # Регистрация счёта в песочнице
	# sandbox.get_sandbox_accounts()  # Счета в песочнице
	# sandbox.close_sandbox_account()  # Закрытие счёта в песочнице
	# sandbox.sandbox_pay_in()  # Пополнение счёта в песочнице
	# sandbox.get_sandbox_operations()  # Выполненные или отменённые операции
	# sandbox.get_sandbox_portfolio()  # Портфель счёта + открытые позиции
	# sandbox.get_sandbox_positions()  # Список позиций счёта
	# sandbox.post_sandbox_order()  # Выставление торгового поручения в песочнице
	# sandbox.get_sandbox_orders()  # Список невыполненных торговых поручений
	# sandbox.get_sandbox_order_state()  # Информация о заявке
	# sandbox.cancel_sandbox_order()  # Отмена торгового поручения в песочнице
