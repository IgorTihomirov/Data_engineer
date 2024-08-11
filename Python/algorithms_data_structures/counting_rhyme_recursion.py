def counting(n, k: int) -> int:
    # Базовый случай.
    if n == 1:
        return 0
    else:
        return (counting(n - 1, k) + k) % n  # рекурсия и расчет индекса


def find_last(n, k: int) -> int:
    # Рекурсивная функция возвращает индекс, поэтому добавляем 1 для корректного номера
    return counting(n, k) + 1


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    result = find_last(n, k)
    print(result)
