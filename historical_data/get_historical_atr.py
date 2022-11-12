import pandas as pd

from ta.volatility import average_true_range


def get_atr(name):
    df = pd.read_csv(f'{name}/{name}_candles.csv')

    atr = average_true_range(high=df['Максимум'], low=df['Минимум'], close=df['Цена закрытия'], window=10)
    df = pd.DataFrame({'ATR': atr, 'Date': df['Время']})

    df.to_csv(f'{name}/{name}_atr.csv', index=False)


get_atr('lukoil')
get_atr('rusal')
get_atr('surgut')
