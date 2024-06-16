# Объявите функцию get_season(), принимающую на вход название месяца;
# функция должна вернуть название сезона, которому принадлежит месяц
# или строку "Ошибка в написании месяца!"

# Место для вашего кода
def get_season(name_month):
    if name_month == 'январь' or name_month == 'февраль' or name_month == 'декабрь':
        return 'зима'
    elif name_month == 'март' or name_month == 'апрель' or name_month == 'май':
        return 'весна'
    elif name_month == 'июнь' or name_month == 'июль' or name_month == 'август':
        return 'лето'
    elif name_month == 'сентябрь' or name_month == 'октябрь' or name_month == 'ноябрь':
        return 'осень'
    else:
        return 'Ошибка в написании месяца!'
# Для контроля вызовем функцию и напечатаем результат.
print(get_season('июнь'))
print(get_season('мартобрь'))