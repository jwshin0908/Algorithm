import sys
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    k = int(input().rstrip())
    print('=' * k)