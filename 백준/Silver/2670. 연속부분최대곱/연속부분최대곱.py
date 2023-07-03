import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = [float(input().rstrip()) for _ in range(n)]
d = array

for i in range(1, n):
    d[i] = max(d[i], d[i] * d[i - 1])

print(f"{max(d):.3f}")