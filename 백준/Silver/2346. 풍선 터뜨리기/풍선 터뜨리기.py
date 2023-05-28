# deque.rotate 사용
from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
d = deque(enumerate(map(int, input().split())))
result = []

while d:
    idx, num = d.popleft()
    result.append(idx + 1)
    # 시계 반대 방향
    if num > 0:
        d.rotate(-(num - 1))
    # 시계 방향
    elif num < 0:
        d.rotate(-num)
print(' '.join(map(str, result)))