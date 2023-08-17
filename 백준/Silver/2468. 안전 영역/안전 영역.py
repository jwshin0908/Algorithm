import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input().rstrip())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))
    
def dfs(graph, visited, x, y, h):
    visited[x][y] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < N):
            if (graph[nx][ny] > h) and (visited[nx][ny] == 0):
                visited[nx][ny] = 1
                dfs(graph, visited, nx, ny, h)

cnt = 0        
for h in range(max(map(max, graph))):
    cnt_temp = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (graph[i][j] > h) and (visited[i][j] == 0):
                cnt_temp += 1
                dfs(graph, visited, i, j, h)
    cnt = max(cnt, cnt_temp)

print(cnt)