# heap은 최솟값을 출력하므로 -를 붙여서 입력 이후, -를 붙여서 출력해줘야 최대 힙 가능

import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())
heap = []

for _ in range(n):
    x = int(input().rstrip())
    
    if x > 0:
        heapq.heappush(heap, -x)
    else:
        if len(heap) != 0:
            print(-heapq.heappop(heap))
        else:
            print(0)
