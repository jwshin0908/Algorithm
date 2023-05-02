from collections import deque
import sys
input = sys.stdin.readline

test = int(input().rstrip())

for _ in range(test):
    n, m = map(int, input().rstrip().split())
    queue = deque(list(map(int, input().rstrip().split())))
    index = deque(list(range(n)))
    cnt = 0
    while queue:
        if queue[0] == max(queue):
            cnt += 1
            queue.popleft()
            if m == index.popleft():
                print(cnt)
        else:
            queue.append(queue.popleft())
            index.append(index.popleft())