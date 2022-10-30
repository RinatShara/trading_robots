import pandas as pd

from ta.trend import ema_indicator


df = pd.read_csv('lukoil/lukoil_candles.csv')

ema = ema_indicator(close=df['Цена закрытия'], window=200)
df = pd.DataFrame({'EMA': ema, 'Date': df['Время']})[199:]

df.to_csv('lukoil/lukoil_ema.csv')
