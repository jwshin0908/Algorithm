from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = []
queue = deque()
dist = 0
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

def bfs():
    while queue:
        x, y = queue.popleft()
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs()
dist = max(map(max, graph))

print(dist - 1)