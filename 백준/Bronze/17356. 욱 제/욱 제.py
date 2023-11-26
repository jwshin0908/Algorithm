import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())
M = (B - A) / 400

print(1 / (1 + 10**M))