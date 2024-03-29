import sqlite3
import sys
import pandas as pd

from datetime import datetime

from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QCompleter, QWidget, QLabel

from Project.design.choose_mode_design import Ui_ChooseModeWindow
from Project.design.testing_mode_design import Ui_TestingWindow
from Project.design.wait_window_design import Ui_WaitWindow
from Project.design.history_tests_design import Ui_HistoryTestsWindow
from Project.design.set_params_design import Ui_StrategyParamsWindow
from Project.design.certain_result_design import Ui_CertainResultWindow

from tinkoff.invest import Client
from tokens import ro_token
from testing import Testing
from data_base.save_result import SavingResult


class LoadWindow(QWidget):
    def __init__(self):
        super(LoadWindow, self).__init__()
        self.setFixedSize(545, 346)
        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap('D:/PRIMARY/Desktop/УИР/Торговые роботы/Project/design/Icons/logo.png'))

        timer = QTimer(self)
        timer.singleShot(5000, self.open_choose_mode)

    def open_choose_mode(self):
        self.close()
        self.choose_example = ChooseWindow()
        self.choose_example.show()


class ChooseWindow(QMainWindow, Ui_ChooseModeWindow):
    def __init__(self):
        super(ChooseWindow, self).__init__()
        self.setupUi(self)
        self.toggle_window()
        self.initial_items()

    def initial_items(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.time)
        self.timer.start(60000)

        date = datetime.now()
        self.current_date.setText(f'{str(date.day).rjust(2, "0")}.{str(date.month).rjust(2, "0")}.{str(date.year)}')
        self.dollar_price.setText(str(round(dollar.units + dollar.nano / 1e9, 2)))
        self.euro_price.setText(str(round(euro.units + euro.nano / 1e9, 2)))

    def time(self):
        time = QTime.currentTime()
        self.current_time.setText(time.toString(Qt.DefaultLocaleShortDate))

    def toggle_window(self):
        self.test_btn.clicked.connect(self.open_test_mode)

    def open_test_mode(self):
        self.test_window = TestingWindow()
        self.test_window.show()
        self.hide()


class TestingWindow(QMainWindow, Ui_TestingWindow):
    def __init__(self):
        super(TestingWindow, self).__init__()
        self.setupUi(self)
        self.initial_items()
        self.add_functions()
        self.autocomplete_share()
        self.toggle_window()

    def initial_items(self):
        self.choose_strat.setCurrentText(parameters[0])
        self.choose_share.setText(parameters[1])
        self.first_date_btn.setText(parameters[2])
        self.second_date_btn.setText(parameters[3])

        self.error_label.setVisible(False)
        self.first_calendar.setVisible(False)
        self.second_calendar.setVisible(False)

        self.timer = QTimer()
        self.timer.timeout.connect(self.time)
        self.timer.start(60000)

        date = datetime.now()
        self.current_date.setText(f'{str(date.day).rjust(2, "0")}.{str(date.month).rjust(2, "0")}.{str(date.year)}')
        self.dollar_price.setText(str(round(dollar.units + dollar.nano / 1e9, 2)))
        self.euro_price.setText(str(round(euro.units + euro.nano / 1e9, 2)))

    def time(self):
        time = QTime.currentTime()
        self.current_time.setText(time.toString(Qt.DefaultLocaleShortDate))

    def add_functions(self):
        self.first_date_btn.clicked.connect(self.show_calendar_1)
        self.second_date_btn.clicked.connect(self.show_calendar_2)
        self.first_calendar.selectionChanged.connect(self.change_date_1)
        self.second_calendar.selectionChanged.connect(self.change_date_2)
        self.reset_btn.clicked.connect(self.reset_values)
        self.start_btn.clicked.connect(self.test_preparing)

    def show_calendar_1(self):
        self.first_calendar.setVisible(True)
        self.second_calendar.setVisible(False)
        self.set_param_btn.setVisible(False)
        self.reset_btn.setVisible(False)
        self.start_btn.setVisible(False)

    def show_calendar_2(self):
        self.second_calendar.setVisible(True)
        self.first_calendar.setVisible(False)
        self.set_param_btn.setVisible(False)
        self.reset_btn.setVisible(False)
        self.start_btn.setVisible(False)

    def change_date_1(self):
        date = self.first_calendar.selectedDate()
        self.first_calendar.setSelectedDate(date)
        self.first_date_btn.setText(f'{str(date.day()).rjust(2, "0")}.{str(date.month()).rjust(2, "0")}.{date.year()}')
        self.first_calendar.setVisible(False)
        self.set_param_btn.setVisible(True)
        self.reset_btn.setVisible(True)
        self.start_btn.setVisible(True)

    def change_date_2(self):
        date = self.second_calendar.selectedDate()
        self.second_calendar.setSelectedDate(date)
        self.second_date_btn.setText(f'{str(date.day()).rjust(2, "0")}.{str(date.month()).rjust(2, "0")}.{date.year()}')
        self.second_calendar.setVisible(False)
        self.set_param_btn.setVisible(True)
        self.reset_btn.setVisible(True)
        self.start_btn.setVisible(True)

    def autocomplete_share(self):
        connection = sqlite3.connect('D:/PRIMARY/Desktop/УИР/Торговые роботы/Project/data_base/shares.db')
        cur = connection.cursor()
        self.shares = [str(*item).lower() for item in cur.execute('''SELECT name FROM shares''')]
        connection.close()
        completer = QCompleter(self.shares, self.choose_share)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setCompletionMode(QCompleter.InlineCompletion)
        self.choose_share.setCompleter(completer)

    def reset_values(self):
        global parameters

        self.error_label.setVisible(False)
        self.choose_strat.setCurrentIndex(0)
        self.choose_share.setText('')
        self.first_date_btn.setText('Задать начальную дату')
        self.second_date_btn.setText('Задать конечную дату')
        parameters = ['', '', 'Задать начальную дату', 'Задать конечную дату', '', '', '']

    def test_preparing(self):
        first_date = self.first_date_btn.text().split('.')
        second_date = self.second_date_btn.text().split('.')

        if self.choose_strat.currentText() == 'Releasing':
            self.error_label.setVisible(True)
            self.error_label.setText('Стратегия в разработке')

        elif self.choose_share.text().lower() not in self.shares:
            self.error_label.setVisible(True)
            self.error_label.setText('Неверно задана акция')

        elif first_date == ['Задать начальную дату'] or second_date == ['Задать конечную дату']:
            self.error_label.setVisible(True)
            self.error_label.setText('Неверно заданы даты')

        elif datetime(*list(map(int, first_date))[::-1]) > datetime(*list(map(int, second_date))[::-1]):
            self.error_label.setVisible(True)
            self.error_label.setText('Неверно заданы даты')

        elif not all(parameters[4:]):
            self.error_label.setVisible(True)
            self.error_label.setText('Нет доп.параметров')

        else:
            parameters[0] = self.choose_strat.currentText()
            parameters[1] = self.choose_share.text().lower()
            parameters[2] = self.first_date_btn.text()
            parameters[3] = self.second_date_btn.text()
            self.error_label.setVisible(False)
            self.wait_window = WaitWindow()
            self.wait_window.show()
            self.hide()

            timer = QTimer(self)
            timer.singleShot(1, self.start_testing)

    def start_testing(self):
        self.open_certain_result(Testing(parameters).get_result())
        self.wait_window.close()

    def toggle_window(self):
        self.hist_tests_btn.clicked.connect(self.open_hist_tests)
        self.set_param_btn.clicked.connect(self.open_set_params)

    def open_hist_tests(self):
        parameters[0] = self.choose_strat.currentText()
        parameters[1] = self.choose_share.text().lower()
        parameters[2] = self.first_date_btn.text()
        parameters[3] = self.second_date_btn.text()

        self.hist_tests = HistoryTestsWindow()
        self.hist_tests.show()
        self.hide()

    def open_set_params(self):
        parameters[0] = self.choose_strat.currentText()
        parameters[1] = self.choose_share.text().lower()
        parameters[2] = self.first_date_btn.text()
        parameters[3] = self.second_date_btn.text()

        self.set_params = StrategyParamsWindow()
        self.set_params.show()
        self.hide()

    def open_certain_result(self, result):
        self.certain_result = CertainResultWindow(result)
        self.certain_result.show()
        self.hide()


class WaitWindow(QMainWindow, Ui_WaitWindow):
    def __init__(self):
        super(WaitWindow, self).__init__()
        self.setupUi(self)


class HistoryTestsWindow(QMainWindow, Ui_HistoryTestsWindow):
    def __init__(self):
        super(HistoryTestsWindow, self).__init__()
        self.setupUi(self)
        self.add_functions()
        self.edit_table()
        self.toggle_window()

    def add_functions(self):
        self.detailed_btn.clicked.connect(self.create_certain_result)

    def edit_table(self):
        sizes = [100, 100, 210, 160, 140, 120, 100]
        self.general_table.setRowCount(0)

        connection = sqlite3.connect('data_base/history_results.db')
        cur = connection.cursor()
        result = cur.execute('''SELECT * FROM gen_tests''').fetchall()

        for i, row in enumerate(result):
            self.general_table.setRowCount(self.general_table.rowCount() + 1)
            for j, item in enumerate(row[1:]):
                self.general_table.setColumnWidth(j, sizes[j])
                self.general_table.setItem(i, j, QTableWidgetItem(str(item)))
        connection.close()

    def create_certain_result(self):
        gen_result = tuple(item.text() for item in self.general_table.selectedItems())
        connection = sqlite3.connect('data_base/history_results.db')
        cur = connection.cursor()
        test_id = cur.execute('''
                        SELECT gen_id
                        FROM gen_tests 
                        WHERE strategy = ? AND company = ? AND period = ? 
                        AND money = ? AND percent = ? AND risk_profit = ? AND profit = ?''', gen_result).fetchall()

        det_result = cur.execute(f'''SELECT * FROM det_tests WHERE det_id = "{test_id[0][0]}"''').fetchall()
        long_det = []
        short_det = []
        for row in list(map(lambda x: list(x)[1:], det_result)):
            if 'LONG' in row:
                long_det.append(row)
                short_det.append([])
            elif 'SHORT' in row:
                short_det.append(row)
                long_det.append([])

        det_result = pd.DataFrame({'Long-сделки': long_det, 'Short-сделки': short_det})
        info = list(*cur.execute(f'''SELECT * FROM info WHERE info_id = "{test_id[0][0]}"'''))[1:]

        self.open_certain_result((det_result, info))

    def toggle_window(self):
        self.return_btn.clicked.connect(self.open_test_window)

    def open_test_window(self):
        self.test_window = TestingWindow()
        self.test_window.show()
        self.hide()

    def open_certain_result(self, result):
        self.certain_result = CertainResultWindow(result)
        self.certain_result.show()
        self.hide()


class StrategyParamsWindow(QMainWindow, Ui_StrategyParamsWindow):
    def __init__(self):
        super(StrategyParamsWindow, self).__init__()
        self.setupUi(self)
        self.initial_items()
        self.add_functions()
        self.toggle_window()
        self.money, self.percent, self.risk_profit = parameters[4:]

    def initial_items(self):
        self.set_money.setText(parameters[4])
        self.set_deal_money.setText(parameters[5])
        self.set_risk_profit.setText(parameters[6])
        self.error_label.setVisible(False)

    def add_functions(self):
        self.set_money.textChanged.connect(self.checking_values)
        self.set_deal_money.textChanged.connect(self.checking_values)
        self.set_risk_profit.textChanged.connect(self.checking_values)

    def checking_values(self):
        self.money = self.set_money.text().replace(',', '.')
        self.percent = self.set_deal_money.text().replace(',', '.').replace('%', '')
        self.risk_profit = self.set_risk_profit.text().replace(',', '.')

        try:
            if self.money and self.percent and self.risk_profit:
                float(self.money)
                float(self.percent)
                float(self.risk_profit)
            if self.percent and float(self.percent) > 100.0:
                self.error_label.setVisible(True)
                self.return_btn.setVisible(False)
            else:
                self.error_label.setVisible(False)
                self.return_btn.setVisible(True)

        except ValueError:
            self.error_label.setVisible(True)
            self.return_btn.setVisible(False)

    def toggle_window(self):
        self.return_btn.clicked.connect(self.open_test_window)

    def open_test_window(self):
        parameters[4] = self.money
        parameters[5] = self.percent
        parameters[6] = self.risk_profit

        self.test_window = TestingWindow()
        self.test_window.show()
        self.hide()


class CertainResultWindow(QMainWindow, Ui_CertainResultWindow):
    def __init__(self, result):
        super(CertainResultWindow, self).__init__()
        self.setupUi(self)
        self.result = result
        self.add_functions()
        self.show_result()
        self.toggle_window()

    def add_functions(self):
        self.save_btn.clicked.connect(self.save_result)

    def show_result(self):
        self.det_params = []
        sizes = [150, 100, 100, 100, 100, 170, 130]
        self.detailed_table.setRowCount(0)

        for i, row in self.result[0].iterrows():
            row_info = []
            self.detailed_table.setRowCount(self.detailed_table.rowCount() + 1)
            if row['Long-сделки']:
                for j, value in enumerate(row['Long-сделки']):
                    row_info.append(value)
                    self.detailed_table.setColumnWidth(j, sizes[j])
                    self.detailed_table.setItem(i, j, QTableWidgetItem(str(value)))
            elif row['Short-сделки']:
                for j, value in enumerate(row['Short-сделки']):
                    row_info.append(value)
                    self.detailed_table.setColumnWidth(j, sizes[j])
                    self.detailed_table.setItem(i, j, QTableWidgetItem(str(value)))
            self.det_params.append(row_info)

        self.long_info.setText(str(self.result[1][0]))
        self.short_info.setText(str(self.result[1][1]))
        self.take_prof_info.setText(str(self.result[1][2]))
        self.stop_info.setText(str(self.result[1][3]))
        self.money_info.setText(str(self.result[1][4]))
        self.profit_info.setText(str(self.result[1][5]))

    def save_result(self):
        edit_parameters = parameters[:2] + [f'{parameters[2]} - {parameters[3]}'] + parameters[4:]  # Объединение дат
        gen_params = edit_parameters + [str(self.result[1][5])]  # Параметры + прибыль
        det_params = self.det_params  # Подробный результат (получили из show_result)
        info = self.result[1]
        result = SavingResult(gen_params, det_params, info).save_all()

        if result:
            self.save_btn.setText('Результат сохранён')
        elif not result:
            self.save_btn.setText('Результат уже сохранён')

    def toggle_window(self):
        self.return_btn.clicked.connect(self.open_test_window)

    def open_test_window(self):
        self.test_window = TestingWindow()
        self.test_window.show()
        self.hide()


if __name__ == '__main__':
    with Client(ro_token) as client:
        dollar = client.market_data.get_last_prices(figi=['BBG0013HGFT4']).last_prices[0].price
        euro = client.market_data.get_last_prices(figi=['BBG0013HJJ31']).last_prices[0].price
    parameters = ['', '', 'Задать начальную дату', 'Задать конечную дату', '', '', '']
    app = QApplication(sys.argv)
    load = LoadWindow()
    load.show()
    sys.exit(app.exec())
