import sys
input = sys.stdin.readline

N, X = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))
result = []

for i in range(N - 1):
    min_value = array[i] + array[i + 1]
    result.append(min_value)

print(min(result) * X)