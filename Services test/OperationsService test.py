from datetime import datetime, timedelta

from tinkoff.invest import Client, GenerateBrokerReportRequest, GetBrokerReportRequest, \
	GenerateDividendsForeignIssuerReportRequest, GetDividendsForeignIssuerReportRequest

from tokens import ro_token, sb_token

with Client(ro_token) as client:
	class OperationService:
		def get_operations(self):
			get_operations = client.operations.get_operations(
				account_id='2006363341',
				from_=datetime(2020, 9, 22, 0, 0, 0),
				to=datetime(2022, 9, 23, 0, 0, 0),
				# state=1,
				# figi='BBG000BBQCY0'
			)
			print(get_operations)

		def get_portfolio(self):
			get_portfolio = client.operations.get_portfolio(account_id='2006363341')
			print(get_portfolio)

		def get_positions(self):
			get_positions = client.operations.get_positions(account_id='2006363341')
			print(get_positions)

		def get_withdraw_limits(self):
			get_withdraw_limits = client.operations.get_withdraw_limits(account_id='2006363341')
			print(get_withdraw_limits)

		def get_broker_report(self):
			get_broker_report = client.operations.get_broker_report(
				generate_broker_report_request=GenerateBrokerReportRequest(account_id='2006363341',
				                                                           from_=datetime.utcnow() - timedelta(days=31),
				                                                           to=datetime.utcnow()),
				get_broker_report_request=GetBrokerReportRequest(task_id='f81f873a-a6a7-4a50-9f38-a47de490d75e')
			)
			print(get_broker_report)

		def get_dividends_foreign_issuer(self):
			get_dividends_foreign_issuer = client.operations.get_dividends_foreign_issuer(
				generate_div_foreign_issuer_report=
				GenerateDividendsForeignIssuerReportRequest(account_id='2006363341',
				                                            from_=datetime.utcnow() - timedelta(days=31),
				                                            to=datetime.utcnow() - timedelta(days=4)),
				get_div_foreign_issuer_report=
				GetDividendsForeignIssuerReportRequest(task_id='6faac979-3df2-463f-814e-11a6359b79fb')
			)
			print(get_dividends_foreign_issuer)


	operation_service = OperationService()

	# operation_service.get_operations()  # Выполненные или отменённые операции
	# operation_service.get_portfolio()  # Портфель счёта + открытые позиции
	# operation_service.get_positions()  # Список позиций счёта
	# operation_service.get_withdraw_limits()  # Доступный остаток для вывода средств
	# operation_service.get_broker_report()  # Брокерский отчёт
	# operation_service.get_dividends_foreign_issuer()  # Отчёт "Справка о доходах за пределами РФ"
