import pandas as pd

from ta.trend import ema_indicator


def get_ema(name):
    df = pd.read_csv(f'{name}/{name}_candles.csv')

    ema = ema_indicator(close=df['Цена закрытия'], window=200)
    df = pd.DataFrame({'EMA': ema, 'Date': df['Время']})[199:]

    df.to_csv(f'{name}/{name}_ema.csv', index=False)


get_ema('lukoil')
get_ema('rusal')
get_ema('surgut')

