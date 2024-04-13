from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
visited = [[0] * M for _ in range(N)]
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def in_range(x, y):
    return (0 <= x and x < N) and (0 <= y and y < M)

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = -1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny) and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = -1

def cheeze():
    for x in range(N):
        for y in range(M):
            cnt = 0
            if graph[x][y] == 1:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if in_range(nx, ny) and visited[nx][ny] == -1:
                        cnt += 1
            if cnt >= 2:
                graph[x][y] = 0

def simulate():
    for i in range(N):
        for j in range(M):
            visited[i][j] = 0
    bfs()
    cheeze()


time = 0
while True:
    cheeze_num = 0
    for row in graph:
        cheeze_num += sum(row)
    if cheeze_num == 0:
        break
    simulate()
    time += 1


print(time)