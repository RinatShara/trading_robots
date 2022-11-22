import pandas as pd
import numpy as np

# Создание Series
a = pd.Series(['One', 'Two', 'Three', 'Four'])
print(a)
a = pd.Series(['One', 'Two', 'Three', 'Four'], index=['A', 'B', 'C', 'D'])
print(a)
print(a.index)
a = pd.Series({'A': 'One', 'B': 'Two', 'C': 'Three', 'D': 'Four'})
print(a)
print(a.dtype)
print(a.shape)
print(a.size)
print(a.ndim)
print(a.to_numpy())
print('#######################')

# Индексы и выборка
a = pd.Series(np.random.randint(0, 10, 5), index=['A', 'B', 'C', 'D', 'E'])
print(a, '\n')
print(a[1], '\n')
print(a[1:4], '\n')
print(a[a > 5], '\n')
print(a[(a > 5) & (a < 9)], '\n')
print(a['A'], '\n')
print(a[['A', 'B']], '\n')
print(a[[1, 0]])
print('#######################')

# Операции
a = pd.Series(np.random.randint(1, 10, 5), index=['A', 'B', 'C', 'D', 'E'])
print(a, '\n')
print(np.sqrt(a), '\n')
print(np.log(a), '\n')
print(np.sin(a), '\n')

a['F'] = 50
print(a, '\n')
a = a.drop(labels=['B', 'F'])  # Можно по индексам: index=[1, 5])
print(a, '\n')

a = pd.Series(np.random.randint(1, 10, 5), index=['A', 'B', 'C', 'D', 'E'])
print(a)
print(a.sum())
print(a.min())
print(a.max())
print(a.mean())

print(a, '\n')
print(a + 2, '\n')
print(a * 2, '\n')
print(a ** 2, '\n')

a.to_csv('pandas_test.historical_candles')
print(pd.read_csv('pandas_test.csv', nrows=1))  # Чо то не робит
a.to_excel('pandas_test.xlsx', sheet_name='Hello_world')
print(pd.read_excel('pandas_test.xlsx', 'Hello_world'))
print('#######################')

# DataFrame
a = pd.DataFrame([[5, 2, 7], [1, 9, 3], [8, 4, 6]])
print(a, '\n')
a = pd.DataFrame([[5, 2, 7], [1, 9, 3], [8, 4, 6]], index=['A', 'B', 'C'], columns=['X', 'Y', 'Z'])
print(a, '\n')
a = pd.DataFrame({'X': [5, 2, 7], 'Y': [1, 9, 3], 'Z': [8, 4, 6]}, index=['A', 'B', 'C'])
print(a, '\n')
print(a.head(2), '\n')  # Показывает первые 2 строки
print(a.tail(2), '\n')  # Показывает последние 2 строки
print(a.info(), '\n')
print(a.describe(), '\n')
print(a.min(), '\n')
print(a.max(), '\n')
print(a.shape)
print(a.size)
print(a.ndim)
print(a.index)
print(a.columns, '\n')
print(a.value_counts('X'), '\n')  # Значения столба с индексом Х и их количество (слева - значение; справа - количество)
print(a['X'].unique())  # Уникальные значения столба с индексом Х
print(a['X'].nunique(), '\n')  # Количество различных значений столба с индексом Х
print(a['Y'].apply(lambda x: x + 2))  # Применение функции lambda к значениям из столба Y
print('#######################')

# Индексация и фильтрация в DataFrame
a = pd.DataFrame({'X': [5, 2, 7], 'Y': [1, 9, 3], 'Z': [8, 4, 6]}, index=['A', 'B', 'C'])
print(a, '\n')
print(a['Z'], '\n')  # Обращение по столбцам
print(a[['Z', 'X']], '\n')
print(a.loc['A'], '\n')  # Обращение по строкам через именнованные
print(a.iloc[0], '\n')  # Обращение по строкам через индексы по умолчанию (0, 1, 2, 3....)
print(a.iloc[1:3, 0:2], '\n')  # Выдаёт 1 и 2 столбцы 2 и 3 строки
print(a.loc['A':'B', 'Y'], '\n')  # Выдаёт ячейки строк А, В и С столбца Y
print(a[a.Z > 5], '\n')  # Выдаёт те строки, в которых у столба Z число больше 5
print(a[a.Z > 5]['X'], '\n')  # Выдаёт значения из столба Х у тех строк, в которых у столба Z число больше 5
a['New_Column'] = (a['X'] + a['Y']) / a['Z']
print(a, '\n')
print(a.sum(), '\n')
print(a.min(), '\n')
print(a.max(), '\n')
print(a.mean(), '\n')
print(a['X'].mean(), '\n')
a = a.drop(['New_Column'], axis=1)
print(a, '\n')
print('#######################')


# Обработка пустых значений
a = pd.DataFrame({
	'X': [4, None, 0],
	'Y': [1, 9, 3],
	'Z': [None, 5, None]}, index=['A', 'B', 'C'])
print(a, '\n')
print(a.isna(), '\n')  # Возвращает DataFrame, но вместо значений: True (если значение ячейки = None) или False
print(a.dropna(axis=1), '\n')  # Выкидывает все столбцы, где есть хоть 1 None
a = a.fillna(a['X'].mean())  # Заменяет все ячейки с None на среднее значение столбца Х
print(a, '\n')
print('#######################')

# Группировка и сортировка
a = pd.DataFrame({'X': [9, 6, 0],
                  'Y': [3, 5, 1],
                  'Z': [6, 5, 5]}, index=['A', 'B', 'C'])
print(a, '\n')
print(a.sort_values('A', ascending=False, axis=1), '\n')  # Сортирует строку А по убыванию <- ascending=False
print(a.groupby(['Z']).count())  # Не знаю даже что делает
print('#######################')

# Объединение и комбинации
a = pd.DataFrame({'X': [9, 6, 0],
                  'Y': [3, 5, 1],
                  'Z': [6, 5, 5]}, index=['A', 'B', 'C'])
print(a, '\n')
b = pd.DataFrame({'O': [0, 0, 0], 'Q': [1, 1, 1]}, index=['A', 'B', 'C'])
a = pd.concat([a, b], axis=1)
print(a, '\n')
print('#######################')
a = pd.DataFrame({'X': [9, 6, 0],
                  'Y': [3, 5, 1],
                  'Z': [6, 5, 5]}, index=['A', 'B', 'C'])
print(a, '\n')
b = pd.DataFrame({'X': [0, 0, 0], 'Y': [1, 1, 1], 'Z': [2, 2, 2]}, index=['D', 'E', 'F'])
a = pd.concat([a, b], axis=0)
print(a, '\n')
print('#######################')
