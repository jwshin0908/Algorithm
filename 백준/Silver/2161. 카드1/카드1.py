import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

array = deque([i for i in range(1, n + 1)])
result = []
while True:
    if len(array) == 1:
        break
    result.append(array.popleft())
    array.append(array.popleft())

final = result + list(array)

print(' '.join(map(str, final)))