# Напишите функцию planting_plan(rows),
# которая принимает на вход количество рядов rows
# и возвращает список с расстояниями в метрах от начала грядки
# до каждого ряда. Первый ряд должен быть размещён в двух метрах от начала грядки.
def planting_plan(rows):
    rows1 = range(2, rows * 2 + 2, 2)
    list_rows = list(rows1)
    return list_rows


print(planting_plan(5))