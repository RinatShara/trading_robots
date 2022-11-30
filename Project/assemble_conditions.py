import pandas as pd
from numpy import sign


class Conditions:
    def __init__(self, data, delta, max_distance):
        self.history = data  # DataFrame, который вернул нам assemble_data.py
        self.delta = delta  # Параметр, отвечающий за разницей между двумя свечами для находждения направления ЕМА
        self.max_distance = max_distance  # Параметр, отвечающий за максимально допустимое расстояние между ценой и ЕМА
        # Финальный DataFrame с условиями, который вернётся в качестве результата работы класса
        self.df = pd.DataFrame({'Время': self.history['Время'],
                                'Цена закрытия': self.history['Цена закрытия'],
                                'EMA': self.history['EMA']})

    def direction_ema_condition(self):  # Расчёт направления ЕМА
        directions = []
        # Считаем разницу двух ЕМА, находящихся на расстоянии delta
        for i in range(self.delta, len(self.df['EMA'])):
            delta_y = self.df['EMA'].values[i] - self.df['EMA'].values[i - self.delta]

            if delta_y >= 0:
                directions.append('Вверх')
            else:
                directions.append('Вниз')
        # Добавляем пустые строки, чтобы длины были одинаковы для конкатенации
        directions = [''] * (len(self.df['EMA']) - len(directions)) + directions
        df = pd.DataFrame({'Направление': directions})
        # Добавляем условие направления ЕМА в финальный DF
        self.df = pd.concat([self.df, df], axis=1)

    def ema_distance_condition(self):  # Расчёт расстояния между ЕМА и ценой
        # Находим расстояние в процентах
        df = pd.DataFrame({"Процент": abs(self.df["Цена закрытия"] - self.df["EMA"]) / self.df['EMA'] * 100})
        # Проверяем, допустимое ли расстояние между ЕМА и ценой
        is_close = []
        for subtraction in df["Процент"]:
            if subtraction >= self.max_distance:
                is_close.append(False)
            elif subtraction < self.max_distance:
                is_close.append(True)
        # Добавляем пустые строки, чтобы длины были одинаковы для конкатенации
        is_close = [False] * (len(self.df['EMA']) - len(is_close)) + is_close
        df_2 = pd.DataFrame({"Достаточное расстояние": is_close})
        # Добавляем условие расстояния в финальный DF
        self.df = pd.concat([self.df, df, df_2], axis=1)

    def macd_condition(self):  # Отлавливание пересечения MACD
        # Получаем значения MACD из DF с историей
        df = pd.DataFrame({'Value Classic': self.history['Value Classic'],
                           'Value Signal': self.history['Value Signal']})
        df_2 = pd.DataFrame({'Разница': df['Value Classic'] - df['Value Signal']})

        intersections = []
        for i in range(len(df_2)):
            if sign(df_2.values[i - 1]) != sign(df_2.values[i]) and i >= 34:  # Пересечение = смена знака разности линий
                if df['Value Classic'].values[i] > 0:  # Местоположение пересечения определяем по основной линии
                    intersections.append('Выше')
                else:
                    intersections.append('Ниже')
            else:
                intersections.append(False)
        df_3 = pd.DataFrame({'Пересечение': intersections})
        # Добавляем условие MACD в финальный DF
        self.df = pd.concat([self.df, df, df_2, df_3], axis=1)

    def super_trend_condition(self):  # Определение цвета Super Trendа
        # Получаем значения Super Trenda из DF с историей
        df = pd.DataFrame({"SuperTrend": self.history['SuperTrend']})

        colors = []
        for color in self.history['Цвет']:
            if color == 1:
                colors.append('Зелёный')
            if color == -1:
                colors.append('Красный')

        df_2 = pd.DataFrame({"Цвет": colors})
        # Добавляем условие Super Trenda финальный DF
        self.df = pd.concat([self.df, df, df_2], axis=1)

    def upper_lower_condition(self):  # Определение местоположения цена относительно ЕМА
        # Находим разницу между ценой и значением ЕМА для каждой свечи
        df = pd.DataFrame({"Разница": self.df["Цена закрытия"] - self.df["EMA"]})

        up_or_low = [""] * 199  # Выравнивание длины списка с длиной финального DF
        for subtraction in df["Разница"]:
            if subtraction > 0:
                up_or_low.append("Выше")
            elif subtraction < 0:
                up_or_low.append("Ниже")
        df_2 = pd.DataFrame({"Выше/Ниже": up_or_low})
        # Добавляем условие местоположения цены в финальный DF
        self.df = pd.concat([self.df, df, df_2], axis=1)

    def assemble(self):  # Вызываем все функции по получению условий
        self.direction_ema_condition()
        self.ema_distance_condition()
        self.macd_condition()
        self.super_trend_condition()
        self.upper_lower_condition()

        return self.df  # Возвращем DF со всеми условиями
