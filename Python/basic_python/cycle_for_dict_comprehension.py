# В цикле for перебираем последовательность range(3),
# по очереди передаём значение каждого элемента в переменную value,
# для каждого элемента словаря создаём ключ и значение:
new_collection = {f'Ключ {value}': f'Значение {value}' for value in range(3)}

print(new_collection)


# или

vegetables = ['Помидор', 'Огурец', 'Капуста']
category = 'Овощная культура'

vegetables_info = {vegetable: category for vegetable in vegetables}
#       Создаём     ключ    и  значение.

print(vegetables_info)