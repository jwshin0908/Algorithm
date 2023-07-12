import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
heap = []

for _ in range(n):
    x = int(input().rstrip())
    # (a, b) tuple : a값을 먼저 비교하고 b값을 비교
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)