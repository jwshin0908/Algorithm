import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
x = int(input().rstrip())

result = 0
array.sort()
start, end = 0, n - 1

while start < end:
    if array[start] + array[end] > x:
        end -= 1
    elif array[start] + array[end] < x:
        start += 1
    elif array[start] + array[end] == x:
        result += 1
        end -= 1
        start += 1

print(result)