import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = []
W_list = []
B_list = []

for _ in range(M):
    graph.append(list(input().rstrip()))

def dfs(graph, x, y, team):
    global cnt
    graph[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if graph[nx][ny] == team:
                cnt += 1
                dfs(graph, nx, ny, team)

for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            cnt = 1
            dfs(graph, i, j, 'W')
            W_list.append(cnt ** 2)
        elif graph[i][j] == 'B':
            cnt = 1
            dfs(graph, i, j, 'B')
            B_list.append(cnt ** 2)

print(sum(W_list), sum(B_list))