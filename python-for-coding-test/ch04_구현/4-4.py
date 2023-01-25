# 4-3. 게임 개발(p.118)
# 못 풀었음. 해설 참고하기

N, M = map(int, input().split())
x, y, direction = map(int, input().split())

# 방문 위치 저장 용도의 N x M 맵 생성(0으로 모두 초기화)
d = [[0] * M for _ in range(N)]
d[x][y] = 1  # 현재 좌표는 방문한 것으로 처리(=1)

# 맵 정보 입력
array = []
for i in range(N):
  array.append(list(map(int, input().split())))

# 방향 정의 - 0(북), 1(동), 2(남), 3(서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전 function
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3


# 시뮬레이션 start
cnt = 1
turn_time = 0
while True:
  # 왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전 이후에 정면에 안 가본 칸이 있을 경우 이동 O
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    cnt += 1
    turn_time = 0
    continue
  # 안 가본 칸이 없거나 바다인 경우
  else:
    turn_time += 1
  # 4개의 방향 모두 갈 곳이 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 돌아갈 수 있다면 이동 O
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0

print(cnt)
