# 4-1. 상하좌우(p.110)
N = int(input())
move = input().split()

# 시작 좌표 지정
x, y = 1, 1

# 방향 지정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direction = ['L', 'R', 'U', 'D']

for i in move:
  index = direction.index(i)
  nx = x + dx[index]
  ny = y + dy[index]
  # N x N 공간 내에 있을 경우에만 이동 확정
  if 1 <= nx <= N and 1 <= ny <= N:
    x, y = nx, ny

print(x, y)
