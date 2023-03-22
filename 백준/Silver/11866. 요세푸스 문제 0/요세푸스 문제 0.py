import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())

array = deque([i for i in range(1, n + 1)])
result = []

while len(array) > 1:
    for _ in range(k - 1):
        array.append(array.popleft())
    result.append(array.popleft())

result.append(array.popleft())

print('<' + ', '.join(map(str, result)) + '>')