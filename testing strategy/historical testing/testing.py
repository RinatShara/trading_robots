import pandas as pd


def testing(money, amount, profit_coeff, *data):
    initial_money = money
    df = pd.DataFrame({'Время': data[0]['Время'], 'Цена закрытия': data[0]['Цена закрытия']})

    names = ['Направление', 'Выше/Ниже', 'Пересечение', 'Расстояние', 'Цвет']
    long_condition = ['Вверх', 'Выше', 'Ниже', True, 'Зелёный']
    short_condition = ['Вниз', 'Ниже', 'Выше', True, 'Красный']

    buy_count = 0
    sell_count = 0

    take_count = 0
    stop_count = 0

    buy_results = []
    sell_results = []
    deals = []

    active_deals = []

    for i, row in data[0].iterrows():
        deal = []
        current_price = row['Цена закрытия']
        candle = [row['Направление'], row['Выше/Ниже'], row['Пересечение'], row['Достаточное расстояние'], row['Цвет']]

        if active_deals:
            for price_range in active_deals:

                if current_price >= price_range[2]:
                    deal.append(f'Take-profit, продал за {current_price * amount}, покупал за {price_range[0]}')
                    take_count += 1
                    money += current_price * amount
                    active_deals.remove(price_range)

                elif current_price < price_range[1]:
                    deal.append(f'Stop-loss, продал за {current_price * amount}, покупал за {price_range[0]}')
                    stop_count += 1
                    money += current_price * amount
                    active_deals.remove(price_range)

        if candle == long_condition and (money - current_price * amount >= 0):
            take_profit = (current_price - row["SuperTrend"]) * profit_coeff + current_price
            stop_loss = row["SuperTrend"]

            money -= current_price * amount
            buy_count += 1

            active_deals.append([current_price, stop_loss, take_profit])

            buy_results.append('Покупка')
            sell_results.append('')
            deal.append(f'Купил на сумму {current_price * amount}, Take-profit: {take_profit}, Stop-loss: {stop_loss}')

        elif candle == short_condition:
            sell_count += 1
            sell_results.append('Продажа')
            buy_results.append('')
            deal.append('')

        else:
            buy_check = list(zip(long_condition, candle))
            sell_check = list(zip(short_condition, candle))

            buy_result = []
            for condition in buy_check:
                if condition[0] != condition[1]:
                    buy_result.append(names[buy_check.index(condition)])

            sell_result = []
            for condition in sell_check:
                if condition[0] != condition[1]:
                    sell_result.append(names[sell_check.index(condition)])

            buy_results.append(buy_result)
            sell_results.append(sell_result)
            deal.append('')

        deals.append(deal)

    df_2 = pd.DataFrame({'Покупка': buy_results, 'Продажа': sell_results, 'Информация': deals})
    df = pd.concat([df, df_2], axis=1)

    df.to_csv(f'results/{data[1]}/{data[1]}_{amount}_{profit_coeff}.csv', index=False)

    print(f'##########Торговля {data[1]}-{initial_money}-{amount}-{profit_coeff}##########')
    print(f'Сколько раз купили: {buy_count}')
    print(f'Сколько раз продали: {sell_count}')
    print(f'Сколько сделок закрыты в плюс: {take_count}')
    print(f'Сколько сделок закрыты в минус: {stop_count}')
    print(f'Изначальное количество денег: {initial_money}')
    print(f'Конечное количество денег: {money}')
    print(f'Прибыль: {money - initial_money}')
    print('___________________')


lukoil_data = (500000, 10, 1.5,
               pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/testing strategy/data/lukoil_conditions.csv'),
               'lukoil')

rusal_data = (500000, 10, 1.15,
              pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/testing strategy/data/rusal_conditions.csv'),
              'rusal')

surgut_data = (500000, 10, 1.15,
               pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/testing strategy/data/surgut_conditions.csv'),
               'surgut')

cinemark_data = (500000, 10, 1.15,
                 pd.read_csv('D:/PRIMARY/Desktop/УИР/Торговые роботы/testing strategy/data/cinemark_conditions.csv'),
                 'cinemark')

testing(*lukoil_data)
# testing(*rusal_data)
# testing(*surgut_data)
# testing(*cinemark_data)
