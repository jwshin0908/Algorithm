import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = []

for _ in range(n):
    array.append(int(input().rstrip()))

array.sort()
result = 0

for i in range(n):
    result += abs((i + 1) - array[i])

print(result)