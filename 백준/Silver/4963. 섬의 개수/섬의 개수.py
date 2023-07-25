import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

def dfs(graph, x, y):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < h) and (0 <= ny < w):
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(graph, nx, ny)

while True:
    w, h = map(int, input().rstrip().split())
    if (w == 0) and (h == 0):
        break
    graph = []
    cnt = 0
    for _ in range(h):
        graph.append(list(map(int, input().rstrip().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(graph, i, j)
                cnt += 1
    print(cnt)