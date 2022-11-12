import pandas as pd
from ta.trend import MACD


def get_macd(name):
    df = pd.read_csv(f"{name}/{name}_candles.csv")

    indicator_macd = MACD(close=df["Цена закрытия"], window_fast=12, window_slow=26, window_sign=9).macd()
    indicator_macd_signal = MACD(close=df["Цена закрытия"], window_fast=12, window_slow=26, window_sign=9).macd_signal()

    df = pd.DataFrame({"Value Classic": indicator_macd, "Value Signal": indicator_macd_signal, "Time": df["Время"]})
    df.to_csv(f'{name}/{name}_macd.csv', index=False)


get_macd('lukoil')
get_macd('rusal')
get_macd('surgut')
