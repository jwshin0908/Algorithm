import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = []
d = [[0] * (M + 1) for _ in range(N + 1)]

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

for i in range(1, N + 1):
    for j in range(1, M + 1):
        d[i][j] = graph[i - 1][j - 1] + max(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])

print(d[N][M])   