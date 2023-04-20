import sys

input = sys.stdin.readline
array = []

for _ in range(9):
    array.append(int(input().rstrip()))

array_sum = sum(array)

for i in range(9):
    for j in range(i + 1, 9):
        if array[i] + array[j] == array_sum - 100:
            extra = [array[i], array[j]]
            break
seven = [i for i in array if i not in extra]

seven.sort()

for i in seven:
    print(i)