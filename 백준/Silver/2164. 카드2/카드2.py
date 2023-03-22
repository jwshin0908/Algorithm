# 큐 자료구조 활용

import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
card = deque([i for i in range(1, n + 1)])

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])
