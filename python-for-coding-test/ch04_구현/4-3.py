# 4-3. 왕실의 나이트(p.115)
# 시뮬레이션(Simulation) 유형

l = str(input())
row = int(l[1])
col = int(ord(l[0])) - int(ord('a')) + 1  # ord : one-charater string에 대한 unicode 반환
cnt = 0

# 나이트가 이동가능한 모든 방향 경우의 수
dir = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for i in dir:
  n_row = row + i[0]
  n_col = col + i[1]
  if 1 <= n_row <= 8 and 1 <= n_col <= 8:  # 새로운 좌표가 공간 내에 있을 경우 cnt 1 추가
    cnt += 1

print(cnt)
