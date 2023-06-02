import sys
input = sys.stdin.readline

x = []
y = []

for _ in range(4):
    x.append(int(input().rstrip()))

for _ in range(2):
    y.append(int(input().rstrip()))

x.sort()
y.sort()

print(int(sum(x) + sum(y) - x[0] - y[0]))