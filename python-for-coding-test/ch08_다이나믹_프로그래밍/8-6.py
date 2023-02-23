# 8-6. 개미 전사(p.220)

n = int(input())
food = list(map(int, input().split()))

# 계산 결과 저장용 DP 테이블
d = [0] * 100

# 다이나믹 프로그래밍(Bottom-Up 방식)
d[1] = food[0]
d[2] = max(food[0], food[1])

for i in range(3, n + 1):
  d[i] = max(d[i - 1], d[i - 2] + food[i - 1])

print(d[i])