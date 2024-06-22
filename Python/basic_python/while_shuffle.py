# Функция shuffle() перемешивает элементы списка случайным образом.
from random import shuffle

# Исходный список:
vegetables = ['Помидор', 'Огурец', 'Баклажан', 'Капуста']
# Создаём отсортированную копию списка,
# с ней будем сравнивать перемешанный список и проверять, отсортирован ли он.
sorted_vegetables = sorted(vegetables)

# Стартовое значение переменной equal ("равенство"). Эта переменная станет True,
# когда перемешанный список окажется равен отсортированному.
equal = False

while not equal:
    print('Перемешиваем...')
    # Элементы списка vegetables перемешаны случайным образом.
    shuffle(vegetables)
    # Посмотрим, в каком порядке оказались элементы.
    print('Вытряхиваем:', vegetables)
    # Выражение с оператором == вернёт значение True или False.
    # Это значение присваиваем переменной equal:
    equal = vegetables == sorted_vegetables
    print()  # Напечатаем пустую строку, чтобы разделить итерации.


print('Бинго!!')