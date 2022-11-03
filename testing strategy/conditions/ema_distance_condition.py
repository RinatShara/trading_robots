import pandas as pd

lukoil_data = pd.read_csv('D:\PRIMARY\Desktop\УИР\Торговые роботы\historical_data\data\лукойл_data.csv'), 'lukoil'
rusal_data = pd.read_csv('D:\PRIMARY\Desktop\УИР\Торговые роботы\historical_data\data\русал_data.csv'), 'rusal'
surgut_data = pd.read_csv(
    'D:\PRIMARY\Desktop\УИР\Торговые роботы\historical_data\data\сургутнефтегаз_data.csv'), 'surgut'


def ema_distance_condition(data):
    is_close = [False] * 199
    df = pd.DataFrame({"Время": data[0]["Время"],
                       "Цена закрытия": data[0]["Цена закрытия"],
                       "EMA": data[0]["EMA"]})
    df_2 = pd.DataFrame({"Процент": abs(df["Цена закрытия"] - df["EMA"]) / df['EMA'] * 100})

    for subtraction in df_2["Процент"]:
        if subtraction >= 5:
            is_close.append(False)
        elif subtraction < 5:
            is_close.append(True)
    df_3 = pd.DataFrame({"Достаточное расстояние": is_close})

    df = pd.concat([df, df_2, df_3], axis=1)
    df.to_csv(f"D:/PyCharm проекты/Торговые роботы/testing strategy/{data[1]}/{data[1]}_ema_distance_condition.csv",
              index=False)


ema_distance_condition(lukoil_data)
ema_distance_condition(rusal_data)
ema_distance_condition(surgut_data)
