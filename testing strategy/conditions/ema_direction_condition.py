import pandas as pd

lukoil_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/lukoil_data.csv'), 'lukoil'
rusal_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/rusal_data.csv'), 'rusal'
surgut_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/surgut_data.csv'), 'surgut'


def direction_ema_condition(data, delta):
    df = pd.DataFrame({'Время': data[0]['Время'],
                       'Цена закрытия': data[0]['Цена закрытия'],
                       'EMA': data[0]['EMA']})

    directions = [''] * (199 + delta)

    for i in range(199 + delta, len(df['EMA'])):
        delta_y = df['EMA'].values[i] - df['EMA'].values[i - delta]

        if delta_y >= 0:
            directions.append('Вверх')
        else:
            directions.append('Вниз')

    df1 = pd.DataFrame({'Направление': directions})

    df = pd.concat([df, df1], axis=1)
    df.to_csv(
        f'D:/PRIMARY/Desktop/УИР/Торговые роботы/testing strategy/{data[1]}/{data[1]}_ema_direction_condition.csv',
        index=False)


direction_ema_condition(lukoil_data, 1)
direction_ema_condition(rusal_data, 1)
direction_ema_condition(surgut_data, 1)
