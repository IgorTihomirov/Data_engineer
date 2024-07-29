import sys

elements_count = int(sys.stdin.readline().rstrip())

data = [None] * elements_count

for index in range(elements_count):
    data[index] = sys.stdin.readline().rstrip()

print(data)