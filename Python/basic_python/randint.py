# Импортировать функцию для получения случайного значения
# и присвоить ей псевдоним rnd
from random import randint as rnd
# Объявить функцию get_dumplings_recommendation(),
# которая вернёт (return) случайное число в диапазоне от 10 до 20.
def get_dumplings_recommendation(min,max):
    quantity = rnd(min,max)
    return quantity
# Вызвать функцию get_dumplings_recommendation() и напечатать заданную фразу.
quantity_dumplings = get_dumplings_recommendation(20, 30)
print('Оптимальным количеством пельменей на сегодня будет', quantity_dumplings)