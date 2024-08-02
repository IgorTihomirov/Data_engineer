array = list(map(int, input().split()))
search_element = int(input())


def find_element(array, search_element):
    """Находит индекс element в отсортированном списке sorted_numbers."""
    # Левая граница (левый индекс) рассматриваемого набора элементов.
    # В начале работы она равна индексу первого элемента в списке.
    left = 0
    # Правая граница (правый индекс) рассматриваемого набора элементов.
    # В начале работы она равна длине списка.
    right = len(array) - 1
    # Допишите код, реализующий бинарный поиск.
    # За основу можно взять код из предыдущего примера.
    while left <= right:
        if int(array[0]) == search_element:
            return 0
        mid = left + (right - left) // 2
        if int(array[mid]) == search_element:
            return mid
        if int(array[mid]) < search_element:
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    print(find_element(array, search_element))
