import pandas as pd

lukoil_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/lukoil_data.csv'), 'lukoil'
rusal_data = pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/rusal_data.csv'), 'rusal'
surgut_data = pd.read_csv(
    'D:/PRIMARY/Desktop/УИР/Торговые роботы/historical_data/data/surgut_data.csv'), 'surgut'


def upper_lower_condition(data):
    df = pd.DataFrame({"Время": data[0]["Время"],
                       "EMA": data[0]["EMA"],
                       "Цена закрытия": data[0]["Цена закрытия"]})
    df_2 = pd.DataFrame({"Разница": df["Цена закрытия"] - df["EMA"]})

    up_or_low = [""] * 199
    for subtraction in df_2["Разница"]:
        if subtraction > 0:
            up_or_low.append("Выше")
        elif subtraction < 0:
            up_or_low.append("Ниже")
    df_3 = pd.DataFrame({"Выше/Ниже": up_or_low})

    df = pd.concat([df, df_2, df_3], axis=1)
    df.to_csv(f"D:/PRIMARY/Desktop/УИР/Торговые роботы/testing strategy/{data[1]}/{data[1]}_upper_lower_condition.csv",
              index=False)


upper_lower_condition(lukoil_data)
upper_lower_condition(rusal_data)
upper_lower_condition(surgut_data)
