# Вместо многоточия укажите нужные параметры.
def find_pool_capacity(length, num_of_people, width=None):
    # Опишите условие, когда передано отрицательное значение длины.
    if length < 0:
        length *= -1
    # Опишите условие, когда передано отрицательное значение
    # количества людей.
    if num_of_people < 0:
        num_of_people *= -1

    # Опишите условие, когда ширина бассейна не указана, когда указано
    # отрицательное значение, и когда положительное.
    if width is None:
        width = length
    elif width < 0:
        width *= -1

    # Опишите условие вывода сообщений и распечатайте эти сообщения.
    if width * length * 2 >= num_of_people:
        print('Бассейн площадью', width * length, 'кв. м. вмещает', num_of_people, 'чел.')
    else: print('Бассейн площадью', width * length, 'кв. м. не вмещает', num_of_people, 'чел.')


# Проверьте работу функции, можете подставить свои значения.
find_pool_capacity(4, 2)
find_pool_capacity(4, 5, 10)
find_pool_capacity(-10, -5, -2)