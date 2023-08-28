import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
heap = []

for _ in range(n):
    a = list(map(int, input().rstrip().split()))
    if a[0] == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(-heapq.heappop(heap))
    else:
        for i in range(a[0]):
            heapq.heappush(heap, - a[i + 1])