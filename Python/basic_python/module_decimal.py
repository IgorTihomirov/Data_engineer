# Из модуля decimal импортируйте тип данных Decimal и параметр getcontext.
# Из модуля math импортируйте константу "пи".
from decimal import Decimal, getcontext
from math import pi
# Приведите константу "пи" к типу Decimal.
# Помните, что Decimal() принимает строку, а константа "пи" - это число.
pipi = Decimal(str(pi))
# Установите необходимую точность для вычислений.
getcontext().prec = 10

# Объявите функцию ellipse_area() с двумя параметрами.
def ellipse_area(d_big, d_small):
    ellipse_area = pipi * d_big * d_small
    print('Площадь эллипса:', ellipse_area, 'кв.м.')
    return ellipse_area

# Объявите три переменные типа Decimal -
# они должны хранить длины полуосей эллипса и глубину пруда.
d_big = Decimal('2.5')
d_small = Decimal('1.75')
depth = Decimal('0.35')

# Вызовите функцию ellipse_area(), в аргументах передайте длины полуосей эллипса.
area = ellipse_area(d_big, d_small)

# Вычислите объём пруда: площадь * глубина.
volume = area * depth
print('Объем воды для наполнения пруда:', volume, 'куб.м.')