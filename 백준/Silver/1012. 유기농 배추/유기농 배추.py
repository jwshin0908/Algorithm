import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

T = int(input().rstrip())

def dfs(graph, x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(graph, nx, ny)

for _ in range(T):
    M, N, K = map(int, input().rstrip().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    for _ in range(K):
        y, x = map(int, input().rstrip().split())
        graph[x][y] = 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(graph, i, j)
                cnt += 1
    print(cnt)