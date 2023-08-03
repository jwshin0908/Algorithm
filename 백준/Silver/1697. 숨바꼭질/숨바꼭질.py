from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
visited = [0] * 100001

def bfs(start, visited):
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[K])
            break
        dx = [-1, 1, x]
        for i in range(3):
            nx = x + dx[i]
            if (0 <= nx <= 100000):
                if visited[nx] == 0:
                    visited[nx] = visited[x] + 1
                    queue.append(nx)

bfs(N, visited)