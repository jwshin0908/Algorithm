from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(graph, visited, v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[x] + 1
                
bfs(graph, visited, 1)
cnt = 0

for i in range(2, N + 1):
    # 본인 or 친구 or 친구의 친구  / 3가지
    if visited[i] != 0 and visited[i] < 4:
        cnt += 1

print(cnt)