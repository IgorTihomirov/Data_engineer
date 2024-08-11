def fibo_bar(n: int) -> int:
    # Базовый случай.
    if n == 0 or n == 1:
        return 1
    else:
        return fibo_bar(n - 1) + fibo_bar(n - 2)


if __name__ == '__main__':
    gen_num = int(input())
    result = fibo_bar(gen_num)
    print(result)
