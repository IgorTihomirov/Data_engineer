def find_two_indexes(data, expected_sum):
    # Ваше решение?
    for i in range(len(data)):
        for j in range(i+1, len(data)):  # j начинается с i + 1, чтобы не использовать один и тот же элемент дважды
            if data[i] + data[j] == expected_sum:  # Проверяем, если сумма равна целевому значению
                return (i, j)
    return None  # Если пара не найдена


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))