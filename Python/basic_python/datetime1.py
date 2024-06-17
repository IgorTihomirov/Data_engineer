# Допишите нужные импорты.
from datetime import datetime, timedelta

def timedelta_days(datetime_str_1, datetime_str_2):
    # Напишите тело функции.
    datetime_str_1 = '2019/05/10 00:00:00'
    datetime_str_1_datetime = datetime.strptime(datetime_str_1, '%Y/%m/%d %H:%M:%S')
    datetime_str_2 = '2019/10/04 00:00:00'
    datetime_str_2_datetime = datetime.strptime(datetime_str_2, '%Y/%m/%d %H:%M:%S')
    return int(timedelta.total_seconds(datetime_str_2_datetime - datetime_str_1_datetime) / 86400)

difference = timedelta_days('2019/05/10 00:00:00', '2019/10/04 00:00:00')

print('От начала посевной до начала сбора урожая прошло', difference, 'дней.')