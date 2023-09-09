from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    array = list(input().rstrip().split())
    queue = deque()
    queue.append(array[0])
    first = array[0]
    for i in range(1, N):
        if first >= array[i]:
            queue.appendleft(array[i])
            first = array[i]
        else:
            queue.append(array[i])
    print(''.join(queue))