import pandas as pd
import pandas_ta as pd_ta

from ta.volatility import average_true_range
from ta.trend import ema_indicator, MACD
from tinkoff.invest import Client
from tokens import ro_token, sb_token
from time import sleep
from datetime import datetime, timezone, timedelta


class HistoricalData:
    def __init__(self, figi):
        self.figi = figi  # Мы получаем только figi и с ними работаем
        self.instruments = {}  # Это словарь кэша, в котором будет хранится информация из функции add_active
        self.df = pd.DataFrame([])  # Это финальный DataFrame, который в конце преобразуется в csv файл

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
        with Client(ro_token) as client:
            df = pd.DataFrame([])  # Финальный DataFrame со свечами
            today = datetime(2022, 10, 22)  # Конечная дата будет 22 октября 2022 года

            for i in range(2, -1, -1):  # Обходим лимитную политику в 300 дней
                for day in range(299, -1, -1):  # Получаем значения за 300 дней
                    # Получаем свечи за определённый день (больше одного дня с 15 минутным интервалом брать нельзя)
                    # Интервал 15 минут, но берём каждую вторую свечу и получаем тем самым 30-минутные свечи
                    candles = client.market_data.get_candles(figi=self.figi,
                                                             from_=today - timedelta(days=day + 300 * i + 1),
                                                             to=today - timedelta(days=day + 300 * i),
                                                             interval=3).candles[::2]
                    # Создаём DataFrame с определёнными значениями свечи
                    df1 = pd.DataFrame([{'Название': self.get_name(self.figi),
                                         'Валюта': self.get_currency(self.figi),
                                         'Время': self.convert_time(item.time),
                                         'Цена открытия': self.convert_money(item.open),
                                         'Цена закрытия': self.convert_money(item.close),
                                         'Минимум': self.convert_money(item.low),
                                         'Максимум': self.convert_money(item.high)} for item in candles])
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

    def assemble(self):  # Главная функция, которая всё и будет считать
        self.get_candles()
        self.get_ema()
        self.get_atr()
        self.get_macd()
        self.get_super_trend()

        name = self.get_name(self.figi)  # Имя итогового csv файла будет совпадать с именем акции
        self.df.to_csv(f'data/{name.lower()}_data.csv', index=False)  # Сохраняем итоговый DF в csv файл


lukoil = HistoricalData('BBG004731032')
lukoil.assemble()

rusal = HistoricalData('BBG008F2T3T2')
rusal.assemble()

surgut = HistoricalData('BBG0047315D0')
surgut.assemble()
