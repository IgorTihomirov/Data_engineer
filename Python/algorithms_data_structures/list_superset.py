def list_superset(list_set_1, list_set_2):
    # Не меняйте названия функции и параметров. Напишите решение здесь.
    if len(list_set_1) >= len(list_set_2):
        list_main, list_subset = list_set_1, list_set_2
    else:
        list_main, list_subset = list_set_2, list_set_1

    if all([i in list_main for i in list_subset]):
        if len(list_main) == len(list_subset):
            return 'Наборы равны.'
        else:
            return f'Набор {list_main} - cупермножество.'
    else:
        return 'Супермножество не обнаружено.'


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
