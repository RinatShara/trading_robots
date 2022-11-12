import pandas as pd

from tinkoff.invest import Client
from tokens import ro_token, sb_token
from time import sleep
from datetime import datetime, timezone, timedelta

lukoil = 'BBG004731032', 'lukoil'
rusal = 'BBG008F2T3T2', 'rusal'
surgut = 'BBG0047315D0', 'surgut'


def get_candles(data):
    with Client(ro_token) as client:
        instruments = {}

        def convert_money(amount):
            return amount.units + amount.nano / 1e9

        def convert_time(time):
            time = time.replace(tzinfo=timezone.utc)
            tz = datetime.strptime('+0500', '%z').tzinfo
            time = time.astimezone(tz)
            return time

        def add_active(figi):
            instruments[figi] = [client.instruments.get_instrument_by(id_type=1, id=figi).instrument.name,
                                 client.instruments.get_instrument_by(id_type=1, id=figi).instrument.currency,
                                 client.instruments.get_instrument_by(id_type=1, id=figi).instrument.lot]

        def get_name(figi):
            if figi not in instruments.keys():
                add_active(figi)
            return instruments[figi][0]

        def get_currency(figi):
            if figi not in instruments.keys():
                add_active(figi)
            return instruments[figi][1]

        df = pd.DataFrame([])
        for i in range(2, -1, -1):
            for day in range(299, -1, -1):
                candles = client.market_data.get_candles(figi=data[0],
                                                         from_=datetime(2022, 10, 22) - timedelta(
                                                             days=day + 300 * i + 1),
                                                         to=datetime(2022, 10, 22) - timedelta(days=day + 300 * i),
                                                         interval=3).candles
                candles_left = candles[::2]
                candles_right = candles[1::2]
                candles = list(zip(candles_left, candles_right))

                df1 = pd.DataFrame([{'Название': get_name(data[0]),
                                     'Валюта': get_currency(data[0]),
                                     'Время': convert_time(item[0].time),
                                     'Цена открытия': convert_money(item[0].open),
                                     'Цена закрытия': convert_money(item[1].close),
                                     'Минимум': min(convert_money(item[0].low), convert_money(item[1].low)),
                                     'Максимум': max(convert_money(item[0].high), convert_money(item[1].high))}
                                    for item in candles])
                df = pd.concat([df, df1], axis=0)
            sleep(45.0)

    df.to_csv(f'{data[1]}/{data[1]}_candles.csv', index=False)


get_candles(lukoil)
get_candles(rusal)
get_candles(surgut)
