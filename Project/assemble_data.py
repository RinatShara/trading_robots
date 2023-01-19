import pandas as pd
import pandas_ta as pd_ta

from ta.volatility import average_true_range
from ta.trend import ema_indicator, MACD
from tinkoff.invest import Client
from tokens import ro_token
from time import sleep
from datetime import datetime, timezone, timedelta


class HistoricalData:
    def __init__(self, figi, start_date, stop_date):
        self.figi = figi  # figi инструмента
        self.start_date = datetime(*list(map(int, start_date.split('.')))[::-1])  # С какого числа брать данные
        self.stop_date = datetime(*list(map(int, stop_date.split('.')))[::-1])  # По какое число брать данные
        self.delta_days = (self.stop_date - self.start_date).days + 2  # Разница в днях
        self.instruments = {}  # Это словарь кэша, в котором будет хранится информация из функции add_active
        self.df = pd.DataFrame([])  # Это финальный DataFrame, который вернётся в качестве результата работы класса

    def convert_money(self, amount):  # Данные от TIA приходит в их специальном типе данных и его надо преобразовать
        return amount.units + amount.nano / 1e9

    def convert_time(self, time):  # Преобразуем время из utc+0 в utc+5
        time = time.replace(tzinfo=timezone.utc)
        tz = datetime.strptime('+0500', '%z').tzinfo
        time = time.astimezone(tz)
        return time

    def add_active(self, figi):  # Добавляем в словарь instruments название акции, её валюту и лотность
        with Client(ro_token) as client:
            self.instruments[figi] = [client.instruments.get_instrument_by(id_type=1, id=figi).instrument.name,
                                      client.instruments.get_instrument_by(id_type=1, id=figi).instrument.currency,
                                      client.instruments.get_instrument_by(id_type=1, id=figi).instrument.lot]

    def get_name(self, figi):  # Получаем название акции через её figi
        if figi not in self.instruments.keys():
            self.add_active(figi)
        return self.instruments[figi][0]

    def get_currency(self, figi):  # Получаем валюту акции через её figi
        if figi not in self.instruments.keys():
            self.add_active(figi)
        return self.instruments[figi][1]

    def get_lot(self, figi):  # Получаем лотность акции через её figi
        if figi not in self.instruments.keys():
            self.add_active(figi)
        return self.instruments[figi][2]

    def get_candles(self):  # Функция получения исторических свечей
        # Разбиение времени на отрезки по 279 дней + остаток
        days = []
        while self.delta_days // 279 != 0:
            days.append(279)
            self.delta_days -= 279
        days.append(self.delta_days % 279)

        with Client(ro_token) as client:
            df = pd.DataFrame([])  # Финальный DataFrame со свечами
            # Получаем первые 10 дней перед стартовой датой, чтобы все значения индикаторов были получены к её началу
            for i in range(20, -1, -1):
                candles = client.market_data.get_candles(figi=self.figi,
                                                         from_=self.start_date - timedelta(days=i + 1),
                                                         to=self.start_date - timedelta(days=i),
                                                         interval=3).candles
                candles_left = candles[::2]  # Берём каждую "левую" свечу
                candles_right = candles[1::2]  # Берём каждую "правую" свечу
                candles = list(zip(candles_left, candles_right))  # Компануем каждую "левую" свечу с "правой"
                # Создаём DataFrame с определёнными значениями свечи
                df1 = pd.DataFrame([{'Название': self.get_name(self.figi),
                                     'Валюта': self.get_currency(self.figi),
                                     'Время': self.convert_time(item[0].time),
                                     'Цена открытия': self.convert_money(item[0].open),
                                     'Цена закрытия': self.convert_money(item[1].close),
                                     'Минимум': min(self.convert_money(item[0].low),
                                                    self.convert_money(item[1].low)),
                                     'Максимум': max(self.convert_money(item[0].high),
                                                     self.convert_money(item[1].high))}
                                    for item in candles])
                df = pd.concat([df, df1], axis=0)

            for i, day in enumerate(days):  # Получаем свечи на каждом промежутке, на который мы разбили период теста
                for j in range(day):
                    candles = client.market_data.get_candles(figi=self.figi,
                                                             from_=self.start_date + timedelta(days=j + 279 * i),
                                                             to=self.start_date + timedelta(days=j + 279 * i + 1),
                                                             interval=3).candles  # Получаем все свечи
                    candles_left = candles[::2]  # Берём каждую "левую" свечу
                    candles_right = candles[1::2]  # Берём каждую "правую" свечу
                    candles = list(zip(candles_left, candles_right))  # Компануем каждую "левую" свечу с "правой"
                    # Создаём DataFrame с определёнными значениями свечи
                    df1 = pd.DataFrame([{'Название': self.get_name(self.figi),
                                         'Валюта': self.get_currency(self.figi),
                                         'Время': self.convert_time(item[0].time),
                                         'Цена открытия': self.convert_money(item[0].open),
                                         'Цена закрытия': self.convert_money(item[1].close),
                                         'Минимум': min(self.convert_money(item[0].low),
                                                        self.convert_money(item[1].low)),
                                         'Максимум': max(self.convert_money(item[0].high),
                                                         self.convert_money(item[1].high))}
                                        for item in candles])
                    df = pd.concat([df, df1], axis=0)  # Дополняем значения df значениями df1
                sleep(45.0)  # Обход лимитной политики

        self.df = pd.concat([self.df, df], axis=1)  # Добавляем в самый главный DF наши исторические свечи

    def get_atr(self):  # Функция получения ATR
        atr = average_true_range(high=self.df['Максимум'], low=self.df['Минимум'],
                                 close=self.df['Цена закрытия'],
                                 window=10)
        df = pd.DataFrame({'ATR': atr})  # Создаём буферный DF со значениями ATR для каждой свечи

        self.df = pd.concat([self.df, df], axis=1)  # Добавляем в самый главный DF значения ATR

    def get_ema(self):  # Функция получения EMA
        ema = ema_indicator(close=self.df['Цена закрытия'], window=200)
        df = pd.DataFrame({'EMA': ema})  # Создаём буферный DF со значениями EMA для каждой свечи

        self.df = pd.concat([self.df, df], axis=1)  # Добавляем в самый главный DF значения EMA

    def get_super_trend(self):  # Функция получения Super Trend
        df = pd_ta.supertrend(close=self.df["Цена закрытия"], high=self.df['Максимум'], low=self.df['Минимум'],
                              length=10, multiplier=1.5)
        # Создаём буферный DF со значениями Super Trend для каждой свечи и его цвет
        df = pd.DataFrame({'SuperTrend': df['SUPERT_10_1.5'], 'Цвет': df['SUPERTd_10_1.5']})

        self.df = pd.concat([self.df, df], axis=1)  # Добавляем в самый главный DF значения Super Trend и его цвет

    def get_macd(self):  # Функция получения MACD
        indicator_macd = MACD(close=self.df["Цена закрытия"], window_fast=12, window_slow=26, window_sign=9).macd()
        indicator_macd_signal = MACD(close=self.df["Цена закрытия"], window_fast=12, window_slow=26,
                                     window_sign=9).macd_signal()

        # Создаём буферный DF со значениями MACD для каждой свечи
        df = pd.DataFrame({"Value Classic": indicator_macd, "Value Signal": indicator_macd_signal})

        self.df = pd.concat([self.df, df], axis=1)  # Добавляем в самый главный DF значения MACD

    def assemble(self):  # Вызываем все функции по получению исторических данных
        self.get_candles()
        self.get_ema()
        self.get_atr()
        self.get_macd()
        self.get_super_trend()

        return self.df  # Возвращаем DataFrame со всеми значениями
