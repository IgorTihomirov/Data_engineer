def is_correct_bracket_seq(seq):
    # Стек для хранения открывающих скобок
    stack = []
    # Словарь для соответствия открывающих и закрывающих скобок
    bracket_map = {')': '(', '}': '{', ']': '['}

    for i in seq:
        if i in bracket_map.values():  # Если это открывающая скобка
            stack.append(i)
        elif i in bracket_map.keys():  # Если это закрывающая скобка
            if not stack or stack[-1] != bracket_map[i]:  # Стек пуст или не соответствует
                return False
            stack.pop()  # Убираем соответствующую открывающую скобку из стека

    return len(stack) == 0  # Проверяем, что стек пуст


if __name__ == '__main__':
    bracket_sequence = input()
    # Проверяем правильность скобочной последовательности
    result = is_correct_bracket_seq(bracket_sequence)
    # Выводим результат
    print(result)
