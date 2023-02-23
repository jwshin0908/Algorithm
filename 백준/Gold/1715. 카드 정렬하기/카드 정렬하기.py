# sort를 사용할 경우 시간 초과 발생

import sys
import heapq

n = int(sys.stdin.readline().rstrip())

heap = []
for _ in range(n):
    data = int(sys.stdin.readline().rstrip())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    sum = first + second
    result += sum
    heapq.heappush(heap, sum)

print(result)