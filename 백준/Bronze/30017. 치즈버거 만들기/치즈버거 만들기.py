import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

if A >= B + 1:
    print(B * 2 + 1)
else:
    print(A * 2 - 1)
