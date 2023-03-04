n = int(input())

# 결과 저장용 DP 테이블
d = [0] * 21

# 다이나믹 프로그래밍(Bottom-Up 방식)
d[0] = 0
d[1] = 1

for i in range(2, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])