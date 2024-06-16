# Объявите функцию get_season(), принимающую на вход название месяца;
# функция должна вернуть название сезона, которому принадлежит месяц
# или строку "Ошибка в написании месяца!"

# Место для вашего кода
def get_season(name_month):
    if name_month == 'январь':
        return 'зима'
    elif name_month == 'февраль':
        return 'зима'
    elif name_month == 'декабрь':
        return 'зима'
    elif name_month == 'март':
        return 'весна'
    elif name_month == 'апрель':
        return 'весна'
    elif name_month == 'май':
        return 'весна'
    elif name_month == 'июнь':
        return 'лето'
    elif name_month == 'июль':
        return 'лето'
    elif name_month == 'август':
        return 'лето'
    elif name_month == 'сентябрь':
        return 'осень'
    elif name_month == 'октябрь':
        return 'осень'
    elif name_month == 'ноябрь':
        return 'осень'
    else:
        return 'Ошибка в написании месяца!'
# Для контроля вызовем функцию и напечатаем результат.
print(get_season('июнь'))
print(get_season('мартобрь'))