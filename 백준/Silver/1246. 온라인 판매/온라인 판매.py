import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
array = []

for _ in range(m):
    array.append(int(input().rstrip()))

array.sort(reverse=True)
result = []

for i in range(m):
    if i + 1 <= n:
        result.append((i + 1) * array[i])
    else:
        result.append(n * array[i])

profit = max(result)
price = array[result.index(profit)]

print(price, profit)