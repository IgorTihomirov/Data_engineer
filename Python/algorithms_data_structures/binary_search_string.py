wins = ['алгоритмы', 'будут', 'главным', 'доводом', 'профессионального', 'разработчика']
element = 'главным'

def find_element(sorted_numbers, element):
    """Находит индекс element в отсортированном списке sorted_numbers."""
    # Левая граница (левый индекс) рассматриваемого набора элементов. 
    # В начале работы она равна индексу первого элемента в списке.
    left = 0
    # Правая граница (правый индекс) рассматриваемого набора элементов. 
    # В начале работы она равна длине списка.
    right = len(sorted_numbers)
    # Допишите код, реализующий бинарный поиск.
    # За основу можно взять код из предыдущего примера.
    while left <= right:
        mid = (left + right) // 2
        if sorted_numbers[mid] == element:
            return mid
        if sorted_numbers[mid] < element:
            left = mid + 1
        else:
            right = mid
    return None


print(find_element(wins, element))
