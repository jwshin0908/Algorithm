# 주어진 graph 오른쪽 90도 회전한 것으로 고려

import sys
input = sys.stdin.readline

C, R = map(int, input().rstrip().split())
K = int(input().rstrip())
graph = [[0] * R for _ in range(C)]

if K > C * R:
    print(0)
    sys.exit()

# 동남서북 순서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = y = direction = 0
graph[0][0] = 1

for i in range(2, K + 1):
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if (0 <= nx < C) and (0 <= ny < R) and (graph[nx][ny] == 0):
            graph[nx][ny] = i
            x = nx
            y = ny
            break
        else:
            direction = (direction + 1) % 4
print(x + 1, y + 1)