# 5-10. 음료수 얼려 먹기(p.149)
# 해설 참고

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))


# DFS를 사용해 특정 노드를 방문 후 연결 노드들도 방문
def dfs(x, y):
  # 주어진 범위를 벗어나면 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  # 현재 노드를 방문하지 않았다면
  if graph[x][y] == 0:
    # 해당 노드 방문 처리
    graph[x][y] = 1
    # 상, 하, 좌, 우 위치도 재귀적 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

# 모든 노드에 대해 음료 채우기
result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result+=1

print(result)