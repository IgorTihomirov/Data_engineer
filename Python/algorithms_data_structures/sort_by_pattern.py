def sort_by_pattern(n: int, arr_n: list, m: int, arr_m: list):
    # Шаг 1: Подсчитываем количество каждого контейнера
    count = {}
    for container in arr_n:
        if container in count:
            count[container] += 1
        else:
            count[container] = 1
    # Шаг 2: Создаем результирующий список в соответствии с шаблоном
    result = []
    for number in arr_m:
        if number in count:
            result.extend([number] * count[number])  # Добавляем контейнеры по количеству их вхождений
            del count[number]  # Удаляем, чтобы не добавлять позже

    # Шаг 3: Добавляем оставшиеся контейнеры, не упомянутые в шаблоне
    leftover = []
    for number, quantity in count.items():
        leftover.extend([number] * quantity)

    # Сортируем оставшиеся контейнеры
    leftover.sort()

    # Шаг 4: Объединяем списки
    result.extend(leftover)

    return result


if __name__ == '__main__':
    n = int(input())
    arr_n = list(map(int, input().split()))
    m = int(input())
    arr_m = list(map(int, input().split()))
    result = sort_by_pattern(n, arr_n, m, arr_m)
    print(" ".join(map(str, result)))
