# 3-3. 숫자 카드 게임(p.96)

N, M = map(int, input().split())

data = list() # 행별 min 값을 담을 리스트

for i in range(N):
  data.append(min(list(map(int, input().split())))) # 행별 min 값을 data에 추가

result = max(data) # 행별 min 값을 담은 data 중에서 max 값 반환

print(result)