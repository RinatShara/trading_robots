import sqlite3
from os import getcwd


class SavingResult:
    def __init__(self, gen_prams, det_params, info):
        self.connection = sqlite3.connect(f'{getcwd()}/data_base/history_results.db')
        self.cur = self.connection.cursor()
        self.create_tables()  # Вызываем функцию по созданию таблиц

        self.amount = list(*self.cur.execute('''SELECT COUNT(gen_id) FROM gen_tests'''))  # Порядковый номер теста
        self.gen_params = (int(*self.amount) + 1,) + tuple(gen_prams)  # Задаём параметры тестирования
        # Задаём подробные результаты по каждой сделке
        self.det_params = list(map(lambda x: tuple([int(*self.amount) + 1] + x), det_params))
        self.info = (int(*self.amount) + 1,) + tuple(info)  # Задаём общие результаты теста

    def create_tables(self):  # Создаём таблицы
        # БД c параметрами стратегии
        self.cur.execute('''CREATE TABLE IF NOT EXISTS gen_tests (gen_id INTEGER PRIMARY KEY,
                                                                  strategy TEXT,
                                                                  company TEXT,
                                                                  period TEXT,
                                                                  money TEXT,
                                                                  percent TEXT,
                                                                  risk_profit TEXT,
                                                                  profit TEXT)''')
        # БД c подробными данными по каждой сделке
        self.cur.execute('''CREATE TABLE IF NOT EXISTS det_tests (det_id INTEGER,
                                                                  time TEXT,
                                                                  deal_type TEXT,
                                                                  price TEXT,
                                                                  take_profit TEXT,
                                                                  stop_loss TEXT,
                                                                  amount TEXT,
                                                                  summa TEXT)''')
        # БД с общей информацией тестирования
        self.cur.execute('''CREATE TABLE IF NOT EXISTS info (info_id INTEGER PRIMARY KEY,
                                                             long_count TEXT,
                                                             short_count TEXT,
                                                             take_count TEXT,
                                                             stop_count TEXT,
                                                             money TEXT,
                                                             profit TEXT)''')

    def check_repeat(self):  # Проверка на повторное тестирование по тем же данным
        all_data = self.cur.execute('''SELECT * FROM gen_tests''').fetchall()
        for row in all_data:
            if self.gen_params[1:] == row[1:] or not all(self.gen_params):  # Проверка на повторение данных + наличиние
                return False
        return True

    def save_all(self):  # Сохранение всех таблиц
        if self.check_repeat():
            self.cur.execute(f'''INSERT INTO gen_tests VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', self.gen_params)
            self.cur.executemany(f'''INSERT INTO det_tests VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', self.det_params)
            self.cur.execute(f'''INSERT INTO info VALUES (?, ?, ?, ?, ?, ?, ?)''', self.info)

            self.connection.commit()
            self.connection.close()
            return True  # Возвращаем True, если всё успешно сохранилось
        return False  # Возвращаем False, если такой тест уже был
