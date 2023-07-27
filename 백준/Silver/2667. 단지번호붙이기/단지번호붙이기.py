import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input().rstrip())
graph = []
result = []
cnt = 0

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def dfs(graph, x, y):
    global cnt
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    if (0 <= x < n) and (0 <= y < n):
        if graph[x][y] == 1:
            cnt += 1
            graph[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(graph, nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(graph, i, j)
            result.append(cnt)
            cnt = 0

result.sort()
       
print(len(result))

for i in result:
    print(i)