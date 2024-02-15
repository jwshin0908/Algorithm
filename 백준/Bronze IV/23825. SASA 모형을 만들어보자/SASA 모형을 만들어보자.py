import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
print(min(N, M) // 2)