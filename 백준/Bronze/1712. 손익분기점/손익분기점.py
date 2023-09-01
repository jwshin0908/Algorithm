import sys
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())

if B >= C:
    print(-1)
else:
    result = A // (C - B) + 1
    print(result)