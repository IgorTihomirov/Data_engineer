def main():
    elements_count = int(input())
    array = list((input().split()))
    count = 0
    result = array[:1]  # копирует список до 1 элемента, не отрезая его
    for item in range(1, elements_count):
        if array[item - 1] != array[item]:
            result.append(array[item])
        else:
            count += 1
    result.extend('_' * count)
    print(*result)


if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    main()