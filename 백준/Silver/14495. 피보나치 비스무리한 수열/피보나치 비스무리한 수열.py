import sys
n = int(sys.stdin.readline().rstrip())

# 결과 저장용 DP 테이블
d = [0] * 117

# DP(Bottom-Up)
d[1] = 1
d[2] = 1
d[3] = 1

for i in range(4, n + 1):
    d[i] = d[i - 1] + d[i - 3]

print(d[n])