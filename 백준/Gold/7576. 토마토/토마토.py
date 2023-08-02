from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().rstrip().split())
graph = []
queue = deque([])
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

def bfs(graph):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

bfs(graph)
result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            sys.exit()
        result = max(result, graph[i][j])

print(result - 1)