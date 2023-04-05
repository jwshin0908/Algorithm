from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())

queue = deque([i for i in range(1, n + 1)])
result = []

while True:
    if len(queue) == 0:
        break
    for _ in range(k - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print('<' + ', '.join(map(str, result)) + '>')