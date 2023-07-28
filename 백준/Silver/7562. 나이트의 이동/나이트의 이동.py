from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip())

def bfs(graph, i, j):
    queue = deque()
    queue.append((i, j))
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    while queue:
        x, y = queue.popleft()
        if (x == end_x) and (y == end_y):
            return graph[x][y] - 1
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if (0 <= nx < L) and (0 <= ny < L):
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

for _ in range(T):
    L = int(input().rstrip())
    start_x, start_y = map(int, input().rstrip().split())
    end_x, end_y = map(int, input().rstrip().split())
    graph = [[0] * L for _ in range(L)]
    graph[start_x][start_y] = 1
    print(bfs(graph, start_x, start_y))