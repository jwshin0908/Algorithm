from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

array = [str(i) for i in range(1, n + 1)]
result = list(map(' '.join, combinations(array, m)))

for i in result:
    print(i)
