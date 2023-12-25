import sys
input = sys.stdin.readline

x, y = map(int, input().rstrip().split())

if x <= y:
    print(y - x)
else:
    print(x + y)