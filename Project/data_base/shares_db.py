import pandas as pd
import sqlite3
from tinkoff.invest import Client
from Project.tokens import ro_token
from os import getcwd


with Client(ro_token) as client:
    shares = client.instruments.shares(instrument_status=1).instruments  # Получаем все акции
    # Сохраняем имя компании и figi акции в DF
    df = pd.DataFrame([{"name": item.name.lower(), "figi": item.figi} for item in shares])
    # Сохраняем DF в БД
    conn = sqlite3.connect(f'{getcwd()}/shares.db')
    df.to_sql('shares', conn, if_exists='replace', index=False)
