import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
T = int(input().rstrip())

def dfs(graph, v, cnt):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            cnt = dfs(graph, i, cnt + 1)
    return cnt

for _ in range(T):
    N, M = map(int, input().rstrip().split())
    graph = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    cnt = dfs(graph, 1, 0)
    print(cnt)