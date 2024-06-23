def print_multiplication_table():
    # Напишите код, который напечатает таблицу умножения.
    for a in range(1, 10):
        for b in range(1, 10):
            print(f'{a} * {b} = {a * b}')
        print('----------')


print_multiplication_table()

