import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().rstrip().split())
print(1 - a, 1 - b, 2 - c, 2 - d, 2 - e, 8 - f)