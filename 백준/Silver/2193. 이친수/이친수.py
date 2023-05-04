import sys
N = int(sys.stdin.readline().rstrip())

# 결과 저장용 DP 테이블
d = [0] * 91

# (마지막 자리 1, 마지막 자리 0)
d[1] = (1, 0)
d[2] = (0, 1)

for i in range(3, N + 1):
    d[i] = (d[i - 1][1], sum(d[i - 1]))

print(sum(d[N]))