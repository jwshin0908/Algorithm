# DFS 유형
n = int(input())
m = int(input())

# 각 노드가 방문된 정보(1차원 리스트)
visited = [False] * (n + 1)

# 각 노드가 연결된 정보(2차원 리스트)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 구현
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
dfs(graph, 1, visited)

if sum(visited)==0:
    print(0)
else:
    print(sum(visited) - 1)