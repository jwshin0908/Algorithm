import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
answer = [0] * (N + 1)
cnt = 1

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    global cnt
    visited[v] = 1
    answer[v] = cnt
    graph[v].sort(reverse = True)
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)

dfs(graph, R, visited)

for i in answer[1:]:
    print(i)