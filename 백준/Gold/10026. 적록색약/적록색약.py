import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().rstrip())
graph = []

for _ in range(N):
    graph.append(list(input().rstrip()))
    
def dfs(graph, visited, x, y):
    visited[x][y] = 1
    color = graph[x][y]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < N):
            if visited[nx][ny] == 0:
                if graph[nx][ny] == color:
                    dfs(graph, visited, nx, ny)

visited = [[0] * N for _ in range(N)]
cnt_1 = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(graph, visited, i, j)
            cnt_1 += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
            
visited = [[0] * N for _ in range(N)]
cnt_2 = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(graph, visited, i, j)
            cnt_2 += 1
            
print(cnt_1, cnt_2)