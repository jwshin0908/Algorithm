# Q05. 볼링공 고르기(p.315)
# 해설도 읽어보기(p.512)

N, M = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  # 오름차순으로 볼링공 무게 정렬
cnt = 0

for i in data:  # 낮은 무게부터 차례대로 i에 투입
  cnt += len([j for j in data if j > i])  # i보다 큰 무게를 B가 선택하는 경우의 수

print(cnt)