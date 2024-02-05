import sys
input = sys.stdin.readline

N = int(input().rstrip())

for _ in range(N):
    A, B, X = map(int, input().rstrip().split())
    result = A * (X - 1) + B
    print(result)