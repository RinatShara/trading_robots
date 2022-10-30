import matplotlib.pyplot as plt
import numpy as np

# Создание рисунка
fig, ax = plt.subplots()
plt.show()

# Создание нескольких графиков
fig_1, new_ax = plt.subplots(2, 2)
plt.show()

# Рисование графика
figure = plt.figure(num=1, figsize=(10, 7), facecolor='yellow', edgecolor='red')
ax_1 = figure.add_subplot(2, 2, 1)
ax_3 = figure.add_subplot(2, 2, 3)
x_1 = np.arange(0, 6)
y_1 = np.arange(0, 6)
x_2 = np.arange(-5, 5.5, 0.5)
y_2 = x_2 ** 2
x_abs = np.arange(-3, 4)
y_abs = np.arange(-3, 4)
ax_1.plot(x_1, y_1)
ax_1.plot(x_2, y_2)
ax_3.plot(x_abs, y_abs)

plt.show()

# Стилизация графика
figure = plt.figure(figsize=(10, 7))  # Размер в дюймах (1 дюйм = 96 пикселей)
ax_1 = figure.add_subplot(4, 2, 1)
ax_2 = figure.add_subplot(4, 2, 2)
ax_3 = figure.add_subplot(4, 2, 3)
ax_4 = figure.add_subplot(4, 2, 4)
ax_5 = figure.add_subplot(4, 2, 5)
ax_6 = figure.add_subplot(4, 2, 6)
ax_7 = figure.add_subplot(4, 2, 7)
ax_8 = figure.add_subplot(4, 2, 8)

x = np.arange(-5, 5.5, 0.5)
y = x ** 2

ax_1.plot(x, y, color='red')
ax_2.plot(x, y, linestyle='-.')
ax_3.plot(x, y, color='green', linestyle='-.')  # '-', '--', '-.', ':', 'solid', 'dashed', 'dashdot', 'dotted'
ax_4.plot(x, np.cos(x), color='green', linestyle='dotted')
ax_5.plot(x, y, marker='*')
ax_6.plot(x, y, color='purple', alpha=0.2)
ax_7.plot(x, y, color='orange', linewidth=3)
ax_8.plot(x, y, color='black', linestyle=':', marker='+', alpha=0.5, linewidth=2.5)

plt.show()

# Лимиты осей
figure = plt.figure(figsize=(10, 7))
ax_1 = figure.add_subplot()

x = np.arange(-5, 5.5, 0.5)
y = x ** 3

ax_1.plot(x, y, color='black', marker='o')
ax_1.set_xlim(-2, 3)
ax_1.set_ylim(-5, 5)

plt.show()

# Подписи и метки
figure = plt.figure(figsize=(10, 7))
ax_1 = figure.add_subplot()

x = np.arange(-5, 5.5, 0.5)
y = x ** 2

ax_1.plot(x, y, color='red', linestyle='dashed', marker='o', label='y = x^2')
ax_1.plot(x, 0.5 * y, color='green', linestyle='solid', marker='*', label='y = 0.5 * x^2')
ax_1.legend(loc='lower right')
ax_1.set_title('Заголовок графика', fontsize='20', font='FangSong')
ax_1.set_xlabel('Ось Х')
ax_1.set_ylabel('Ось Y')

plt.show()

# Рисочки на координатных осях, границы и вспомогательная сетка
figure = plt.figure(figsize=(10, 7))
ax_1 = figure.add_subplot()

x = np.arange(-5, 5.5, 0.5)
y = x ** 2

ax_1.plot(x, y, color='red', linestyle='dashed', marker='o', label='y = x^2')

ax_1.set_xticks(np.arange(-5, 5.5, 0.5))
ax_1.set_yticks(np.arange(0, 27, 1))

ax_1.spines['right'].set_visible(False)
ax_1.spines['top'].set_visible(False)

ax_1.grid(color='black', linewidth=2, linestyle='--')

plt.show()

# Сохранение в картинку
figure = plt.figure(figsize=(10, 7))
ax_1 = figure.add_subplot()

x = np.arange(-5, 5.5, 0.5)
y = x ** 2

ax_1.plot(x, y)
figure.savefig('test.png')

# Столбчатая диаграмма
figure = plt.figure(figsize=(10, 7))
ax_1 = figure.add_subplot(2, 1, 1)
ax_2 = figure.add_subplot(2, 1, 2)

ax_1.bar([1, 2, 3], [7, 6, 10], color='red', label='Vertical bar')
ax_2.barh([1.5, 4], [2, 5], color='red', label='Horizontal bar')
ax_1.legend()
ax_2.legend()

plt.show()
