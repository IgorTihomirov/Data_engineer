# Прочитать число из первой строки входных данных и привести к целочисленному типу.
def main():
    a = int(input())
# Сделать то же самое со второй строкой.
    b = int(input())
    result = a + b
# Напечатать результат - сумму двух чисел.
    print(result)


if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    main()