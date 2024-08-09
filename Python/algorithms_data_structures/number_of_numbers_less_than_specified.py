array = list(map(int, input().split()))


def values_in_array(numbers):
    result = []
    # Проходим по каждому элементу в исходном массиве с индексом i
    for i in range(len(numbers)):
        count = 0
        # Сравниваем текущий элемент с другими элементами j
        for j in range(len(numbers)):
            # Если элемент i больше элемента j, увеличиваем счетчик `count`.
            if numbers[i] > numbers[j]:
                count += 1
        result.append(count)
    return result


if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    print(" ".join(map(str, values_in_array(array))))
