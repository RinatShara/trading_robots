import numpy as np

# Создание массива
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.shape)  # Длина массива
print(arr.dtype)  # Тип объектов в массиве
print(arr.ndim)  # Размерность массива
print(arr.size)  # Количество элементов в массиве
print('######################')

# Махинации с типами данных
arr = np.array([1, 2, 3, 4, 5], dtype=np.float_)
print(arr.dtype)
arr = arr.astype(np.int_)
print(arr.dtype)
print('######################')

# Создание диапозона значений
arr = np.arange(0, 10, 0.5)
print(arr)
arr = np.random.random(5)  # 5 случайных чисел [0; 1)
print(arr)
arr = np.random.random_sample(5)  # 5 случайных неповторяющихся чисел [0; 1)
print(arr)
arr = np.random.randint(5, 10, 7)  # 7 случайных целых чисел [5; 10]
print(arr)
arr = np.linspace(2, 5, 5)  # 5 равноудалённых чисел [2; 5]
print(arr)
arr = (10 - -10) * np.random.random(5) - 10  # 5 случайных чисел [10; -2]
print(arr)
print('######################')

# Операции
arr = np.array([1, 2, 3, 4, 5])
print(np.sqrt(arr))
print(np.sin(arr))
print(np.cos(arr))
print(np.log(arr))
print(np.exp(arr))

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
print(a + b, np.add(a, b))
print(a - b, np.subtract(a, b))
print(a * b, np.multiply(a, b))
print(a / b, np.divide(a, b))

arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)
print(arr ** 2)
print(arr < 3)

arr = np.random.randint(-5, 10, 10)
print(arr)
print(arr.min())
print(arr.max())
print(arr.mean())
print(arr.sum())
print(arr.std())
print(np.median(arr))
print('######################')

# Манипуляции с массивами
arr = np.array([4, 1, 7, 5])
print(arr)
arr = np.insert(arr, 2, 3)  # Вставляем 3 в индекс 2
print(arr)
arr = np.delete(arr, 2)  # Удаляет элемент на 2 индексе
print(arr)
arr = np.sort(arr)
print(arr)
new_arr = np.array([0, 0, 0])
arr = np.concatenate((arr, new_arr))
print(arr)
arr = np.array_split(arr, 3)  # Разбивает массив на 3 части
print(arr)
print('######################')

# Индексы в одномерном массиве
arr = np.array([1, -2, 3, -4, 5])
arr[0] = 0
print(arr)
print(arr[2])
print(arr[0:4])
print(arr[::2])
print(arr[arr < 2])
print(arr[(arr < 2) & (arr > -1)])
print(arr[(arr < 2) | (arr > 4)])
arr[0:3] = 0
print(arr)
print('######################')

# Матрицы и многомерные массивы
matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)], dtype=np.float_)
print(matrix)
print(matrix.shape)
print(matrix.size)
print(matrix.ndim)
print(matrix.dtype)
print('######################')

# Манипуляции с матрицами
matrix = np.reshape(matrix, (1, 9))  # Переформирует матрицу в 1 строку с 9 столбцами
print(matrix)
matrix = np.resize(matrix, (2, 2))  # Образает матрицу до размеров 2 на 2
print(matrix)
print('######################')

# Создание диапозона значений для матриц
matrix = np.random.random((3, 2))  # Матрица 3 на 2 из рандомных чисел [0; 1)
print(matrix)
matrix = np.arange(1, 17).reshape(4, 4)
print(matrix)
print('######################')

# Создание специальных матриц
matrix = np.zeros((2, 3))  # Матрица из нулей размером 2 на 3
print(matrix)
matrix = np.ones((2, 3))  # Матрица из единиц размером 2 на 3
print(matrix)
matrix = np.eye(5)  # Квадратная матрица из нулей 5 на 5 с единицами по диагонали
print(matrix)
matrix = np.full((3, 2), 9)  # Матрица из девяток размером на 2
print(matrix)
matrix = np.empty((3, 2))  # Пустая матрица 3 на 2
print(matrix)
print('######################')

# Операции с матрицами + все те, которые для одномерных массивов
matrix_1 = np.array([(1, 2), (3, 4)])
matrix_2 = np.array([(5, 6), (7, 8)])
print(matrix_1 + matrix_2, np.add(matrix_1, matrix_2), sep='\n')
print(matrix_1 - matrix_2, np.subtract(matrix_1, matrix_2), sep='\n')
print(matrix_1 * matrix_2, np.multiply(matrix_1, matrix_2), sep='\n')
print(matrix_1 / matrix_2, np.divide(matrix_1, matrix_2), sep='\n')
matrix = np.concatenate((matrix_1, matrix_2), axis=0)  # Добавляет matrix_2 к matrix_1 как к строкам
print(matrix)
matrix = np.concatenate((matrix_1, matrix_2), axis=1)  # Добавляет matrix_2 к matrix_1 как к столбцам
print(matrix)

print(matrix_1.dot(matrix_2))  # Скалярное произведение
matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(matrix)
matrix = np.delete(matrix, 1, axis=0)  # Удаляет вторую строку
print(matrix)
matrix = np.delete(matrix, 1, axis=1)  # Удаляет второй стобец
print(matrix)
print(np.split(matrix, 2, axis=1))  # Разбивает матрицу на 2 массива по столбцам

print(np.sqrt(matrix))
print(np.sin(matrix))

print(matrix.min(axis=0))  # Находит минимум по каждому СТОЛБЦУ
print(matrix.max(axis=1))  # Находит максимум по каждой СТРОКЕ
print(matrix.mean(axis=0))  # Находит среднее значение по каждому СТОЛБЦУ
print(matrix.mean(axis=1))  # Находит среднее значение по каждой СТРОКЕ
print('######################')

# Индексация в матрицах
matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(matrix)
print(matrix[1, 2])
print(matrix[2])  # 2 строка
print(matrix[:, 2])  # 2 столбец
print(matrix[1:3, 0:2])  # 1 и 2 столбец 2 и 3 строки
print(matrix[matrix > 5])
print('######################')

# Специальные операции
matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(matrix.T)  # Меняет столбы и строки местами
print(matrix.flatten())  # Превращает матрицу в одномерный массив
print('######################')
