import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = []
cnt = 0

for _ in range(N):
    graph.append(list(input().rstrip()))

def dfs(graph, x, y):
    if graph[x][y] == '-':
        graph[x][y] = 1
        ny = y + 1
        if (0 <= ny < M) and graph[x][ny] == '-':
            dfs(graph, x, ny)
    if graph[x][y] == '|':
        graph[x][y] = 1
        nx = x + 1
        if (0 <= nx < N) and graph[nx][y] == '|':
            dfs(graph, nx, y)
                
for i in range(N):
    for j in range(M):
        if (graph[i][j] == '-') or (graph[i][j] == '|'):
            dfs(graph, i, j)
            cnt += 1

print(cnt)