import sys

n = int(sys.stdin.readline().rstrip())

# 결과 저장용 DP 테이블
d = [0] * 1000001

# DP(Bottom-Up)
d[1] = 1
d[2] = 2

for i in range(3, n + 1):
    d[i] = (d[i - 2] + d[i - 1]) % 15746

print(d[n])