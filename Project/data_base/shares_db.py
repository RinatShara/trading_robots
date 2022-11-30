import sqlite3
from tinkoff.invest import Client
from tokens import ro_token
import pandas as pd


with Client(ro_token) as client:
    shares = client.instruments.shares(instrument_status=1).instruments  # Получаем все акции
    # Сохраняем имя компании и figi акции в DF
    df = pd.DataFrame([{"name": item.name.lower(), "figi": item.figi} for item in shares])
    # Сохраняем DF в БД
    conn = sqlite3.connect('shares.db')
    df.to_sql('shares', conn, if_exists='replace', index=False)
