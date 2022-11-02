import pandas as pd
from numpy import sign

lukoil_data = open('D:\PRIMARY\Desktop\УИР\Торговые роботы\historical_data\data\лукойл_data.csv',
                   encoding='utf-8'), 'lukoil'
rusal_data = open('D:\PRIMARY\Desktop\УИР\Торговые роботы\historical_data\data\русал_data.csv',
                  encoding='utf-8'), 'rusal'
surgut_data = open('D:\PRIMARY\Desktop\УИР\Торговые роботы\historical_data\data\сургутнефтегаз_data.csv',
                   encoding='utf-8'), 'surgut'


def macd_condition(data):
    df = pd.read_csv(data[0])
    df = pd.DataFrame({'Время': df['Время'],
                       'Value Classic': df['Value Classic'],
                       'Value Signal': df['Value Signal']})
    subtractions = pd.DataFrame({
        'Разница': df['Value Classic'] - df['Value Signal']
    })

    intersections = []
    for i in range(len(subtractions)):
        if sign(subtractions.values[i - 1]) != sign(subtractions.values[i]) and i >= 34:
            if df['Value Classic'].values[i] > 0:
                intersections.append('Выше')
            else:
                intersections.append('Ниже')
        else:
            intersections.append(False)

    signs = pd.DataFrame({
        'Пересечение': intersections
    })

    df = pd.concat([df, subtractions, signs], axis=1)
    df.to_csv(f'D:/PRIMARY/Desktop/УИР/Торговые роботы/testing strategy/{data[1]}/{data[1]}_macd_condition.csv',
              index=False)


macd_condition(lukoil_data)
macd_condition(rusal_data)
macd_condition(surgut_data)
