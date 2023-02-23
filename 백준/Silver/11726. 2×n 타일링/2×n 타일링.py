n = int(input())

# 계산 결과 저장용 DP 테이블
d = [0] * 1001

# 다이나믹 프로그래밍(Bottom-Up 방식)
d[1] = 1
d[2] = 2

for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2]) % 10007

print(d[n])