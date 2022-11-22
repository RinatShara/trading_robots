import pandas as pd
from numpy import sign

lukoil_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/lukoil_data.csv'), 'lukoil'
rusal_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/rusal_data.csv'), 'rusal'
surgut_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/surgut_data.csv'), 'surgut'


def macd_condition(data):
    df = pd.DataFrame({'Время': data[0]['Время'],
                       'Value Classic': data[0]['Value Classic'],
                       'Value Signal': data[0]['Value Signal']})
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

    df = pd.concat([df, df_2, df_3], axis=1)
    df.to_csv(f'D:/PRIMARY/Desktop/УИР/Торговые роботы/testing strategy/{data[1]}/{data[1]}_macd_condition.csv',
              index=False)


macd_condition(lukoil_data)
macd_condition(rusal_data)
macd_condition(surgut_data)
