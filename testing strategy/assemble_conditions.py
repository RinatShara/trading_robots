import pandas as pd
from numpy import sign


class Conditions:
    def __init__(self, data, delta, max_distance):
        self.history = data[0]
        self.directory = data[1]
        self.delta = delta
        self.max_distance = max_distance
        self.df = pd.DataFrame({'Время': self.history['Время'],
                                'Цена закрытия': self.history['Цена закрытия'],
                                'EMA': self.history['EMA']})

    def direction_ema_condition(self):
        directions = [''] * (199 + self.delta)

        for i in range(199 + self.delta, len(self.df['EMA'])):
            delta_y = self.df['EMA'].values[i] - self.df['EMA'].values[i - self.delta]

            if delta_y >= 0:
                directions.append('Вверх')
            else:
                directions.append('Вниз')

        df = pd.DataFrame({'Направление': directions})

        self.df = pd.concat([self.df, df], axis=1)

    def ema_distance_condition(self):
        df = pd.DataFrame({"Процент": abs(self.df["Цена закрытия"] - self.df["EMA"]) / self.df['EMA'] * 100})

        is_close = [False] * 199
        for subtraction in df["Процент"]:
            if subtraction >= self.max_distance:
                is_close.append(False)
            elif subtraction < self.max_distance:
                is_close.append(True)

        df_2 = pd.DataFrame({"Достаточное расстояние": is_close})

        self.df = pd.concat([self.df, df, df_2], axis=1)

    def macd_condition(self):
        df = pd.DataFrame({'Value Classic': self.history['Value Classic'],
                           'Value Signal': self.history['Value Signal']})
        df_2 = pd.DataFrame({'Разница': df['Value Classic'] - df['Value Signal']})

        intersections = []
        for i in range(len(df_2)):
            if sign(df_2.values[i - 1]) != sign(df_2.values[i]) and i >= 34:
                if df['Value Classic'].values[i] > 0:
                    intersections.append('Выше')
                else:
                    intersections.append('Ниже')
            else:
                intersections.append(False)

        df_3 = pd.DataFrame({'Пересечение': intersections})

        self.df = pd.concat([self.df, df, df_2, df_3], axis=1)

    def super_trend_condition(self):
        df = pd.DataFrame({"SuperTrend": self.history['SuperTrend']})

        colors = []
        for color in self.history['Цвет']:
            if color == 1:
                colors.append('Зелёный')
            if color == -1:
                colors.append('Красный')

        df_2 = pd.DataFrame({"Цвет": colors})

        self.df = pd.concat([self.df, df, df_2], axis=1)

    def upper_lower_condition(self):
        df = pd.DataFrame({"Разница": self.df["Цена закрытия"] - self.df["EMA"]})

        up_or_low = [""] * 199
        for subtraction in df["Разница"]:
            if subtraction > 0:
                up_or_low.append("Выше")
            elif subtraction < 0:
                up_or_low.append("Ниже")
        df_2 = pd.DataFrame({"Выше/Ниже": up_or_low})

        self.df = pd.concat([self.df, df, df_2], axis=1)

    def assemble(self):
        self.direction_ema_condition()
        self.ema_distance_condition()
        self.macd_condition()
        self.super_trend_condition()
        self.upper_lower_condition()

        self.df.to_csv(f'D:/PRIMARY/Desktop/УИР/Торговые роботы/testing strategy/data/{self.directory}_conditions.csv',
                       index=False)


lukoil_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/lukoil_data.csv'), 'lukoil'
rusal_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/rusal_data.csv'), 'rusal'
surgut_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/surgut_data.csv'), 'surgut'
cinemark_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/cinemark_data.csv'), 'cinemark'

lukoil = Conditions(lukoil_data, 1, 5)
lukoil.assemble()

rusal = Conditions(rusal_data, 1, 5)
rusal.assemble()

surgut = Conditions(surgut_data, 1, 5)
surgut.assemble()

cinemark = Conditions(cinemark_data, 1, 5)
cinemark.assemble()
