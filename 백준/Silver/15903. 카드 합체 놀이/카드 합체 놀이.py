import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
heap = list(map(int, input().rstrip().split()))

heapq.heapify(heap)

for _ in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a + b)
    heapq.heappush(heap, a + b)

print(sum(heap))