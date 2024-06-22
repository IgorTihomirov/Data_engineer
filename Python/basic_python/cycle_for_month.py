# Программа ниже распечатывает названия месяцев.
# Допишите внутри цикла условие, которое будет проверять,
# оканчивается ли название месяца на мягкий знак.
# Если да, программа должна переходить к следующей итерации цикла.
# В итоге программа должна напечатать месяцы без мягкого знака на конце.

months = (
    'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
    'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
)

for month in months:
    if str.endswith(month, 'ь'):
        continue
    print(month)