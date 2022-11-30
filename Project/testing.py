import pandas as pd
import sqlite3

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
        connection = sqlite3.connect('D:/PRIMARY/Desktop/УИР/Торговые роботы/Project/data_base/shares.db')
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
        self.free_money = self.initial_money * float(params[5]) / 100  # params[5] - процент от своб.средств на 1 сделку
        self.profit_coeff = float(params[6])

    def testing(self):  # Тестирование стратеги
        for i, row in self.conditions.iterrows():  # Пробегаемся по каждой строке в DF с условиями
            # Задаём переменные для дальнейшего пользования
            current_price = row['Цена закрытия']
            amount = self.free_money // current_price  # Количество акций, с которыми можно торговать
            candle = [row['Направление'],
                      row['Выше/Ниже'],
                      row['Пересечение'],
                      row['Достаточное расстояние'],
                      row['Цвет']]

            # Проверка на наличие активных сделок
            if self.active_deals:
                for price_range in self.active_deals:
                    if current_price >= price_range[3]:  # Если цена превысила отметку take-profit
                        self.take_count += 1
                        self.money += current_price * amount
                        self.active_deals.remove(price_range)

                    elif current_price < price_range[2]:  # Если цена стала ниже отметки stop-loss
                        self.stop_count += 1
                        self.money += current_price * amount
                        self.active_deals.remove(price_range)

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
                self.active_deals.append([current_price, amount, stop_loss, take_profit])
                # Добавляем информацию по сделке для дальнейшего отображения
                self.long_results.append([time, 'LONG', current_price,
                                          round(take_profit, 2), round(stop_loss, 2), int(amount),
                                          round(current_price * amount, 2)])
                self.short_results.append('')  # Выравнивание длин

            # Проверка условий для short-сделки + проверка на наличие денег для совершения сделки
            elif candle == self.short_condition and (self.money - current_price * amount >= 0):
                # Задаём время совершения сделки, take-profit и stop-loss
                time = f'{str(row["Время"].date().day).rjust(2, "0")}.' \
                       f'{str(row["Время"].date().month).rjust(2, "0")}.{row["Время"].date().year} ' \
                       f'{str(row["Время"].time().hour).rjust(2, "0")}:{str(row["Время"].time().minute).rjust(2, "0")}'
                take_profit = (row["SuperTrend"] - current_price) * self.profit_coeff + current_price
                stop_loss = row["SuperTrend"]

                self.money -= current_price * amount
                self.short_count += 1
                # Добавляем сделку в список активных
                self.active_deals.append([current_price, amount, stop_loss, take_profit])
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
