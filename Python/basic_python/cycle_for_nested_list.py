# Пригодится для наполнения списков!
import random

# 1. Создание списка списков:
areas = 3
rows = 3
harvest = [[random.randint(5, 20) for _ in range(areas)] for _ in range(rows)]  # Примените list comprehension.
print(harvest)


# 2. Функция для подсчёта общего урожая:
def total_harvest(harvest):
    return sum([sum(area) for area in harvest])


# 3. Функция для подсчёта среднего урожая с каждого участка::
def average_harvest_per_plot(harvest):
    return [sum(area) / len(area) for area in harvest]


print('Урожай с каждой грядки на каждом участке:', harvest)
print('Общий урожай со всех участков:', total_harvest(harvest))
print('Средний урожай с каждого участка:', average_harvest_per_plot(harvest))
