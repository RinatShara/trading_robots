from tinkoff.invest import Client
from tokens import ro_token, sb_token

with Client(ro_token) as client:
	class UsersService:
		def get_accounts(self):
			get_accounts = client.users.get_accounts()
			print(get_accounts)

		def get_margin_attributes(self):  # Маржинальная торг. недоступна
			get_margin_attributes = client.users.get_margin_attributes()
			print(get_margin_attributes)

		def get_user_tariff(self):
			get_user_tariff = client.users.get_user_tariff()
			print(get_user_tariff)

		def get_info(self):
			get_info = client.users.get_info()
			print(get_info)

	users_service = UsersService()

	# users_service.get_accounts()  # Все счета пользователя
	# users_service.get_margin_attributes()  # Маржинальные показатели по счёту
	# users_service.get_user_tariff()  # Тариф пользователя
	# users_service.get_info()  # Информация о пользователе
