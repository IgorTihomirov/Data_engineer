any_sequence = [1, 2, 3]
# Список можно распаковать в набор переменных.
# Имена переменных задаёт разработчик.
first, second, third = any_sequence

# Проверим, что получилось:
print(first)
print(second)
print(third)
# А что со списком?
print(any_sequence)

apples_by_day = [61, 58, 56, 34, 67, 50, 74, 64, 78, 69]
# Распакуйте список в набор переменных
one, two, three, four, five, six, seven, eight, nine, ten = apples_by_day

# Напечатайте значения первой и последней переменных.
print('\n',one, ten)