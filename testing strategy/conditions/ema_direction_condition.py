import pandas as pd

lukoil_data = open('D:\PRIMARY\Desktop\УИР\Торговые роботы\historical_data\data\лукойл_data.csv',
                   encoding='utf-8'), 'lukoil'
rusal_data = open('D:\PRIMARY\Desktop\УИР\Торговые роботы\historical_data\data\русал_data.csv',
                  encoding='utf-8'), 'rusal'
surgut_data = open('D:\PRIMARY\Desktop\УИР\Торговые роботы\historical_data\data\сургутнефтегаз_data.csv',
                   encoding='utf-8'), 'surgut'


def direction_ema_condition(data):
    df = pd.read_csv(data[0])
    df = pd.DataFrame({'Время': df['Время'],
                       'Цена закрытия': df['Цена закрытия'],
                       'EMA': df['EMA']})

    directions = [''] * 399

    for i in range(399, len(df['EMA'])):
        great_values = 0
        lower_values = 0
        current_value = df['EMA'].values[i]

        for previous_value in df['EMA'][i - 200: i + 1]:
            if previous_value >= current_value:
                great_values += 1
            if previous_value < current_value:
                lower_values += 1

        if lower_values >= great_values:
            directions.append('Вверх')
        if lower_values < great_values:
            directions.append('Вниз')

    df1 = pd.DataFrame({'Направление': directions})

    df = pd.concat([df, df1], axis=1)
    df.to_csv(
        f'D:/PRIMARY/Desktop/УИР/Торговые роботы/testing strategy/{data[1]}/{data[1]}_ema_direction_condition.csv',
        index=False)


direction_ema_condition(lukoil_data)
direction_ema_condition(rusal_data)
direction_ema_condition(surgut_data)
