# Вместо многоточия укажите необходимые параметры.
def count_tiles(depth, length, width=None):
    # Опишите условие, когда ширина бассейна не указана.
    if width is None:
        width = length
    # Посчитайте, сколько понадобится плиток для стенок и дна бассейна.
    count_tiles_wall = depth * length * 2
    count_tiles_wall_1 = depth * width * 2
    count_tiles_bot = length * width
    total_tiles = count_tiles_wall + count_tiles_bot + count_tiles_wall_1
    # Верните результат работы функции.
    return total_tiles


total_tiles = count_tiles(2, 5)
print('Общее количество плиток для строительства бассейна:', total_tiles)