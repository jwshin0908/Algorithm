import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

print(min(A // 2, B))