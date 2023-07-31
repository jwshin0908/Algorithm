from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
index = list(map(int, input().rstrip().split()))
dq = deque([i for i in range(1, n + 1)])
cnt = 0

for i in index:
    if dq.index(i) >= (len(dq) / 2):
        j = len(dq) - dq.index(i)
        cnt += j
        dq.rotate(j)
    else:
        j = dq.index(i)
        cnt += j
        dq.rotate(-j)
    dq.popleft()

print(cnt)