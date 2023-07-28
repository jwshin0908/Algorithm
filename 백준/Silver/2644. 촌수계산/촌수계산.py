import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().rstrip())
start, end = map(int, input().rstrip().split())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, v, visited):   
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = visited[v] + 1
            dfs(graph, i, visited)
    
visited = [0] * (n + 1)
dfs(graph, start, visited)

if visited[end] >= 1:
    print(visited[end])
else:
    print(-1)