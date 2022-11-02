import pandas as pd

from ta.volatility import average_true_range

df = pd.read_csv('lukoil/lukoil_candles.csv')
atr = average_true_range(high=df['Максимум'], low=df['Минимум'], close=df['Цена закрытия'],
                         window=10)
df = pd.DataFrame({'ATR': atr, 'Date': df['Время']})

df.to_csv('lukoil/lukoil_atr.csv', index=False)
