import sys
n = int(sys.stdin.readline().rstrip())

# 결과 저장용 DP 테이블
d = [0] * 36
d[0] = 1
d[1] = 1

for i in range(2, n + 1):
    for a in range(i):
        b = i - 1 - a
        d[i] += d[a] * d[b]

print(d[n])