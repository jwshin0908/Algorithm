k = int(input())

# 결과 저장용 DP 테이블
d = [0] * 46

# 다이나믹 프로그래밍(Bottom-Up 방식)
d[0] = (1, 0)
d[1] = (0, 1)
d[2] = (1, 1)

for i in range(3, k + 1):
    d[i] = (d[i - 1][1], d[i - 1][0] + d[i - 1][1])

print(d[k][0], d[k][1])