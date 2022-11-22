import pandas as pd

lukoil_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/lukoil_data.csv'), 'lukoil'
rusal_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/rusal_data.csv'), 'rusal'
surgut_data = pd.read_csv(
    'D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/surgut_data.csv'), 'surgut'


def super_trend_condition(data):
    df = pd.DataFrame({"Время": data[0]['Время'],
                       "Цена закрытия": data[0]['Цена закрытия'],
                       "SuperTrend": data[0]['SuperTrend']})

    colors = []
    for color in data[0]["Цвет"]:
        if color == 1:
            colors.append('Зелёный')
        if color == -1:
            colors.append('Красный')
    df_2 = pd.DataFrame({"Цвет": colors})

    df = pd.concat([df, df_2], axis=1)
    df.to_csv(f"D:/PRIMARY/Desktop/УИР/Торговые роботы/testing strategy/{data[1]}/{data[1]}_super_trend_condition.csv",
              index=False)


super_trend_condition(lukoil_data)
super_trend_condition(rusal_data)
super_trend_condition(surgut_data)
