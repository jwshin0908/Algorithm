import sys
import math
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
array = [False] * 1001
result = []

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if array[j] == False:
            array[j] = True
            result.append(j)
        if len(result) >= k:
            break

print(result[k - 1])