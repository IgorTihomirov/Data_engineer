# Пропишите нужные импорты.
from datetime import datetime, timedelta

# Напишите код функции, следуя плану из задания.
def get_results(leader_time, loser_time):
    leader_time1 = datetime.strptime(leader_time, '%H:%M:%S')
    loser_time1 = datetime.strptime(loser_time, '%H:%M:%S')
    delta = int(timedelta.total_seconds(loser_time1 - leader_time1))
    if delta == 0:
        print('Вы пробежали за', leader_time, 'и победили!')
    else:
        hours = delta // 3600 % 24
        minutes = delta // 60 % 60
        seconds = delta % 60
        delta_time = str(hours).zfill(1) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2)
        print('Вы пробежали за', loser_time, 'с отставанием от лидера', delta_time)

# Проверьте работу программы, можете подставить свои значения.
get_results('02:02:02', '02:02:02')
get_results('02:02:02', '03:04:05')