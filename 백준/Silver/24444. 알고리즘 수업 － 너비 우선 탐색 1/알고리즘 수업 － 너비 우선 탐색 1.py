from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 1
def bfs(graph, visited, start):
    global cnt
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        graph[v].sort()
        for i in graph[v]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                queue.append(i)
                
bfs(graph, visited, R)

for v in visited[1:]:
    print(v)