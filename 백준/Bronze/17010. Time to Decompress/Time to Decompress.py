import sys
input = sys.stdin.readline

N = int(input().rstrip())
for _ in range(N):
    x, y = input().split()
    print(y * int(x))