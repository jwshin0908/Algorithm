import sys
t = int(input())
for _ in range(t):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    print(x+y)