import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(graph, v, visited):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(graph, i, visited)
            
dfs(graph, 1, visited)

for i in range(2, N + 1):
    print(visited[i])