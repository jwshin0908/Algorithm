import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

if N == M:
    print(1)
else:
    print(0)