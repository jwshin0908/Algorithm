import sys
n = int(input().rstrip())
array = []
cnt = 0

for _ in range(n):
    array.append(int(input().rstrip()))

for i in range(n - 2, -1, -1):
    if array[i] >= array[i + 1]:
        cnt += (array[i] - array[i + 1] + 1)
        array[i] = array[i + 1] - 1

print(cnt)