from ta.trend import MACD
import pandas as pd

df = pd.read_csv("surgut/surgut_candles.csv")

indicator_macd = MACD(close=df["Цена закрытия"], window_fast=12, window_slow=26, window_sign=9).macd()
indicator_macd_signal = MACD(close=df["Цена закрытия"], window_fast=12, window_slow=26, window_sign=9).macd_signal()

df = pd.DataFrame({"Value Classic": indicator_macd, "Value Signal": indicator_macd_signal, "Time": df["Время"]})
df.to_csv('surgut/surgut_macd.csv', index=False)
