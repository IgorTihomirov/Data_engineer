def find_for_substring(u_string: str):
    char_set = set()  # Множество для хранения уникальных символов
    left_pointer = 0  # Левый указатель окна
    max_length = 0  # Максимальная длина найденной подстроки

    # Перебираем символы в строке с правым указателем
    for right_pointer in range(len(u_string)):
        while u_string[right_pointer] in char_set:  # Пока встречаем дубликат
            char_set.remove(u_string[left_pointer])  # Удаляем левый элемент из множества
            left_pointer += 1  # Сдвигаем левый указатель вперед
      
        char_set.add(u_string[right_pointer])  # Добавляем новый символ в множество
        max_length = max(max_length, right_pointer - left_pointer + 1)  # Обновляем максимальную длину подстроки
    return max_length


if __name__ == '__main__':
    input_string = input()
    print(find_for_substring(input_string))
