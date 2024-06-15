# Импортировать функцию для получения случайного значения
# и присвоить ей псевдоним rnd
from random import randint as rnd
# Объявить функцию get_dumplings_recommendation(),
# которая вернёт (return) случайное число в диапазоне от 10 до 20.
def get_dumplings_recommendation():
    quantity = rnd(10, 20)
    return quantity
# Вызвать функцию get_dumplings_recommendation() и напечатать заданную фразу.
quantity_dumplings = get_dumplings_recommendation()
print('Оптимальным количеством пельменей на сегодня будет', quantity_dumplings)