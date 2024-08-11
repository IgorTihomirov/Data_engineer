def max_blocks(arr):
    n = len(arr)
    max_blocks_count = 0
    current_max = 0

    for i in range(n):
        current_max = max(current_max, arr[i])
        
        # Если текущий индекс совпадает с текущим максимальным элементом,
        # это означает, что мы можем завершить текущий блок.
        if i == current_max:
            max_blocks_count += 1

    return max_blocks_count


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    result = max_blocks(array)
    print(result)
