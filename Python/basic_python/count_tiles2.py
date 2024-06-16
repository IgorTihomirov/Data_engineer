# Код этой функции не меняйте.
def count_tiles(depth, length, width=None):
    if width is None:
        width = length

    width_side = 2 * width * depth
    length_side = 2 * length * depth
    bottom_tiles = length * width
    total = width_side + length_side + bottom_tiles

    return total


# Передайте в функцию нужный параметр и напишите её код.
def make_phrase(total_tiles):
    if total_tiles == 11 or total_tiles == 12 or total_tiles == 13 or total_tiles == 14:
        return str(total_tiles) + ' плиток'
    elif total_tiles % 10 == 1:
        return str(total_tiles) + ' плитку'
    elif total_tiles % 10 == 2 or total_tiles % 10 == 3 or total_tiles % 10 == 4:
        return str(total_tiles) + ' плитки'
    else:
        return str(total_tiles) + ' плиток'


total_tiles = count_tiles(2, 2, 2)
# Выведите на экран нужное сообщение.
print('Для строительства бассейна нужно заготовить', make_phrase(total_tiles))