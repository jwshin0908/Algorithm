from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

def bfs(graph, i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 0
    while queue:
        x, y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (0 <= nx < n) and (0 <= ny < m) and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(graph, i, j)
            
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end = ' ')
        else:
            print(visited[i][j], end = ' ')
    print()