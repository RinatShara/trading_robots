import pandas as pd
import sqlite3
from os import getcwd

from assemble_data import HistoricalData
from assemble_conditions import Conditions


class Testing:
    def __init__(self, params):
        self.params = params  # Параметры стратегии, которые задал пользователь

        self.cond_names = ['Направление', 'Выше/Ниже', 'Пересечение', 'Расстояние', 'Цвет']  # Названия условий
        self.long_condition = ['Вверх', 'Выше', 'Ниже', True, 'Зелёный']  # Значения условий для long-сделки
        self.short_condition = ['Вниз', 'Ниже', 'Выше', True, 'Красный']  # Значения условий для short-сделки

        self.long_count = 0  # Счётчик long-сделок
        self.short_count = 0  # Счётчик short-сделок

        self.take_count = 0  # Счётчик сделок с "плюсом"
        self.stop_count = 0  # Счётчик сделок с "минусом"

        self.long_results = []  # Список с информацией по каждой long-сделке
        self.short_results = []  # Список с информацией по каждой short-сделке

        self.active_deals = []  # Список активных сделок

    def set_testing_params(self, params):  # Определяем оставшиеся параметры для тестирования
        # Получаем figi акции по её имени через БД
        connection = sqlite3.connect(f'{getcwd()}/data_base/shares.db')
        cur = connection.cursor()
        self.share = list(*cur.execute(f'''SELECT figi FROM shares WHERE name = "{params[1]}"'''))
        connection.close()
        # Получаем DF со всеми историческими значениями индикаторов и цены
        self.historical_data = HistoricalData(*self.share, params[2], params[3]).assemble().reset_index(drop=True)
        # Получаем DF со всеми условиями
        self.conditions = Conditions(self.historical_data, 1, 5).assemble()
        # Задаём оставшиеся параметры
        self.initial_money = float(params[4])
        self.money = float(params[4])  # Будет меняться
        self.bag_risk = float(params[5])
        self.profit_coeff = float(params[6])
        self.historical_data.to_csv('hist.csv')
        self.conditions.to_csv('cond.csv')

    def testing(self):  # Тестирование стратегии
        for i, row in self.conditions.iterrows():  # Пробегаемся по каждой строке в DF с условиями
            # Задаём переменные для дальнейшего пользования
            current_price = row['Цена закрытия']
            amount = (self.bag_risk / 100) * self.money // abs(current_price - row["SuperTrend"])  # Количество акций
            if self.money < amount * current_price:  # Если денег не хватает на первое кол-во акций, то другой расчёт
                amount = self.money // current_price
            candle = [row['Направление'],
                      row['Выше/Ниже'],
                      row['Пересечение'],
                      row['Достаточное расстояние'],
                      row['Цвет']]

            # Проверка на наличие активных сделок
            if self.active_deals:
                for deal_info in self.active_deals:
                    if 'long' in deal_info:  # Определяем тип сделки
                        if current_price >= deal_info[3]:  # Если цена достигла отметки take-profit или стала выше
                            self.take_count += 1
                            self.money += current_price * deal_info[1]
                            self.active_deals.remove(deal_info)
                            print(f'Закрыта long с плюсом: {deal_info[0]}')

                        elif current_price <= deal_info[2]:  # Если цена достигла отметки stop-loss или стала ниже
                            self.stop_count += 1
                            self.money += current_price * deal_info[1]
                            self.active_deals.remove(deal_info)
                            print(f'Закрыта long с минусом: {deal_info[0]}')

                    elif 'short' in deal_info:  # Определяем тип сделки
                        if current_price <= deal_info[3]:  # Если цена достигла отметки take-profit или стала ниже
                            if self.money - current_price * deal_info[1] < 0:  # Если не получается выкупить всё кол-во
                                print('yes')
                                buy_amount = self.money // current_price  # Выкупаем столько, сколько позволяет средств
                                self.money -= current_price * buy_amount
                                deal_info[1] -= buy_amount
                            else:  # Иначе выкупаем всё
                                print(f'Закрыта short с плюсом: {deal_info[0]}')
                                self.take_count += 1
                                self.money -= current_price * deal_info[1]
                                self.active_deals.remove(deal_info)

                        elif current_price >= deal_info[2]:  # Если цена достигла отметки stop-loss или стала выше
                            if self.money - current_price * deal_info[1] < 0:  # Если не получается выкупить всё кол-во
                                print('yes')
                                buy_amount = self.money // current_price  # Выкупаем столько, сколько позволяет средств
                                self.money -= current_price * buy_amount
                                deal_info[1] -= buy_amount
                            else:  # Иначе выкупаем всё
                                print(f'Закрыта short с минусом: {deal_info[0]}')
                                self.stop_count += 1
                                self.money -= current_price * deal_info[1]
                                self.active_deals.remove(deal_info)

            # Проверка условий для long-сделки + проверка на наличие денег для совершения сделки
            if candle == self.long_condition and (self.money - current_price * amount >= 0):
                # Задаём время совершения сделки, take-profit и stop-loss
                time = f'{row["Время"].date().day}.{row["Время"].date().month}.{row["Время"].date().year} ' \
                       f'{row["Время"].time().hour}:{row["Время"].time().minute}'
                take_profit = (current_price - row["SuperTrend"]) * self.profit_coeff + current_price
                stop_loss = row["SuperTrend"]

                self.money -= current_price * amount
                self.long_count += 1
                # Добавляем сделку в список активных
                self.active_deals.append([current_price, amount, stop_loss, take_profit, 'long'])
                # Добавляем информацию по сделке для дальнейшего отображения
                self.long_results.append([time, 'LONG', current_price,
                                          round(take_profit, 2), round(stop_loss, 2), int(amount),
                                          round(current_price * amount, 2)])
                self.short_results.append('')  # Выравнивание длин

            # Проверка условий для short-сделки
            elif candle == self.short_condition:
                # Задаём время совершения сделки, take-profit и stop-loss
                time = f'{str(row["Время"].date().day).rjust(2, "0")}.' \
                       f'{str(row["Время"].date().month).rjust(2, "0")}.{row["Время"].date().year} ' \
                       f'{str(row["Время"].time().hour).rjust(2, "0")}:{str(row["Время"].time().minute).rjust(2, "0")}'
                take_profit = current_price - (row["SuperTrend"] - current_price) * self.profit_coeff
                stop_loss = row["SuperTrend"]

                self.money += current_price * amount
                self.short_count += 1
                # Добавляем сделку в список активных
                self.active_deals.append([current_price, amount, stop_loss, take_profit, 'short'])
                # Добавляем информацию по сделке для дальнейшего отображения
                self.short_results.append([time, 'SHORT', current_price,
                                           round(take_profit, 2), round(stop_loss, 2), int(amount),
                                           round(current_price * amount, 2)])
                self.long_results.append('')  # Выравнивание длин

    def get_result(self):  # Получаем результат тестирования
        self.set_testing_params(self.params)  # Вызываем функцию по задаче параметров
        self.testing()  # Вызываем функцию тестирования
        # Добавляем информации по long-сделкам short-сделкам в DF
        df = pd.DataFrame({'Long-сделки': self.long_results,
                           'Short-сделки': self.short_results}).reset_index(drop=True)
        # Добавляем итоговые результаты тестирования в список
        info = [self.long_count,
                self.short_count,
                self.take_count,
                self.stop_count,
                round(self.initial_money, 2),
                round(self.money - self.initial_money)]

        return df, info  # Возвращаем DF с информацией по сделкам и список с результатами тестирования
