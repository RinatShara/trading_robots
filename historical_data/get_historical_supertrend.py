import pandas as pd
import pandas_ta as pd_ta

df_candles = pd.read_csv('surgut/surgut_candles.csv')

super_trend = pd_ta.supertrend(close=df_candles["Цена закрытия"], high=df_candles['Максимум'],
                               low=df_candles['Минимум'],
                               length=10, multiplier=1.5)
super_trend = pd.DataFrame({'SuperTrend': super_trend['SUPERT_10_1.5'], 'Цвет': super_trend['SUPERTd_10_1.5']})
super_trend.to_csv('surgut/surgut_super_trend.csv', index=False)

# import csv
# import pandas as pd
#
# df_candles = pd.read_csv('lukoil/lukoil_candles.csv')
# df_atr = pd.read_csv('lukoil/lukoil_atr.csv')
#
# close = list(map(float, list(df_candles['Цена закрытия'])))[9:]
# high = list(map(float, list(df_candles['Максимум'])))[9:]
# low = list(map(float, list(df_candles['Минимум'])))[9:]
# date = list(df_candles['Время'])
# atr = list(map(float, list(df_atr['ATR'])))
#
# upper_band_basic = [(low[0] + high[0]) / 2 + atr[0] * 1.5]
# lower_band_basic = [(low[0] + high[0]) / 2 - atr[0] * 1.5]
# upper_band = [(low[0] + high[0]) / 2 + atr[0] * 1.5]  # Задаём первые значения для upper_band
# lower_band = [(low[0] + high[0]) / 2 - atr[0] * 1.5]  # Задаём первые значения для lower_band
# supertrend = [lower_band[0]]  # Примем, что первое значение супер тренда равно первому значению lower_band
# color = ['Зелёный']
#
# for i in range(1, len(close)):
#     # Расчёт значения upper_band_basic и lower_band_basic
#     upper_band_basic.append((low[i] + high[i]) / 2 + atr[i] * 1.5)
#     lower_band_basic.append((low[i] + high[i]) / 2 - atr[i] * 1.5)
#
#     # Расчёт значения upper_band
#     if (upper_band_basic[i] < upper_band[i - 1]) or (close[i - 1] > upper_band[i - 1]):
#         upper_band.append(upper_band_basic[i])
#     else:
#         upper_band.append(upper_band[i - 1])
#
#     # Расчёт значения lower_band
#     if (lower_band_basic[i] > lower_band[i - 1]) or (close[i - 1] < lower_band[i - 1]):
#         lower_band.append(lower_band_basic[i])
#     else:
#         lower_band.append(lower_band[i - 1])
#
#     # Расчёт значения supertrend
#     if (supertrend[i - 1] == upper_band[i - 1]) and (close[i] < upper_band[i]):
#         supertrend.append(upper_band[i])
#
#     elif (supertrend[i - 1] == upper_band[i - 1]) and (close[i] > upper_band[i]):
#         supertrend.append(lower_band[i])
#
#     elif (supertrend[i - 1] == lower_band[i - 1]) and (close[i] > lower_band[i]):
#         supertrend.append(lower_band[i])
#
#     elif (supertrend[i - 1] == lower_band[i - 1]) and (close[i] < lower_band[i]):
#         supertrend.append(upper_band[i])
#
#     if abs(supertrend[i] - high[i]) > abs(supertrend[i] - low[i]):
#         color.append('Зелёный')
#
#     else:
#         color.append('Красный')
#
# df = pd.DataFrame({'SuperTrend': pd.Series(supertrend), 'Цвет': pd.Series(color), 'Время': pd.Series(date)})
# df.to_csv('lukoil/lukoil_supertrend.csv', index=False)
