import pandas as pd

from tinkoff.invest import Client
from tokens import ro_token, sb_token
from time import sleep
from datetime import datetime, timezone, timedelta

figi = 'BBG0047315D0'

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


    def get_lot(figi):
        if figi not in instruments.keys():
            add_active(figi)
        return instruments[figi][2]


    df = pd.DataFrame([])
    for i in range(2, -1, -1):
        for day in range(299, -1, -1):
            candles = client.market_data.get_candles(figi=figi,
                                                     from_=datetime(2022, 10, 22) - timedelta(days=day + 300 * i + 1),
                                                     to=datetime(2022, 10, 22) - timedelta(days=day + 300 * i),
                                                     interval=3).candles[::2]
            df1 = pd.DataFrame([{'Название': get_name(figi),
                                 'Валюта': get_currency(figi),
                                 'Время': convert_time(item.time),
                                 'Цена открытия': convert_money(item.open),
                                 'Цена закрытия': convert_money(item.close),
                                 'Минимум': convert_money(item.low),
                                 'Максимум': convert_money(item.high)} for item in candles])
            df = pd.concat([df, df1], axis=0)
        sleep(45.0)

df.to_csv('surgut/surgut_candles.csv')
