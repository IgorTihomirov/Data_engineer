input_data = input()
heights = list(map(int, input_data.split()))


def valid_mountain_array(arr):
    n = len(arr)
    # Проверка на минрмальную длину массива
    if n < 3:
        return False

    # Начальная точка высоты i
    i = 0

    # Восходящий участок
    while i < n - 1 and arr[i] < arr[i + 1]:
        # Добавляем точку в массив, пока высота возрастает и точка находится не в конце горы
        i += 1

    # Проверка, что восходящий участок не пустой и не находится на краю горы
    if i == 0 or i == n - 1:
        return False

    # Нисходящий участок
    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    # Когда последняя точка окажется в конце горы, значит это правильная гора
    return i == n - 1


if valid_mountain_array(heights):
    print(True)
else:
    print(False)

