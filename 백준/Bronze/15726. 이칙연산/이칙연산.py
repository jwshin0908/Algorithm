import sys
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())

print(max(int(A * B / C), int(A / B * C)))