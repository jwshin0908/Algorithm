import sys
input = sys.stdin.readline

n = int(input().rstrip())

# DP 테이블
d = [0] * (n + 2)
d[1] = 1
d[2] = 1

l = [0] * (n + 2)
l[1] = 4
l[2] = 6
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
    l[i] = l[i - 1] + d[i] * 2

print(l[n])