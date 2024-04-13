from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
distance = [[0] * N for _ in range(N)]
food = []
eat_cnt = 0
shark_size = 2
time = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark = (i, j)
            graph[i][j] = 0
def in_range(x, y):
    return (0 <= x and x < N) and (0 <= y and y < N)

def bfs():
    q = deque()
    q.append(shark)
    distance[shark[0]][shark[1]] = 1
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny) and graph[nx][ny] <= shark_size and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))
                if graph[nx][ny] > 0 and graph[nx][ny] < shark_size:
                    food.append((distance[nx][ny], nx, ny))
def eat():
    global eat_cnt, shark_size, time, shark
    food.sort(key = lambda x: (x[0], x[1], x[2]))
    dis, x, y = food[0]
    time += (dis - 1)
    shark = (x, y)
    graph[x][y] = 0
    eat_cnt += 1
    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0

while True:
    food = []
    for i in range(N):
        for j in range(N):
            distance[i][j] = 0
    bfs()
    if len(food) == 0:
        break
    else:
        eat()

print(time)