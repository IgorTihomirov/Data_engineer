# Напишите функцию get_competition_data().
def get_competition_data(data):
    dictionary = data[0]
    a = dict.keys(dictionary)
    sort_a = sorted(a)
    print(f'Команды, участвовавшие в гонке: ' + ', '.join(sort_a))


races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]


get_competition_data(races_data)


