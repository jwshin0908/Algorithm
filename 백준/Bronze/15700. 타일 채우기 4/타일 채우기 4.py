import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
result = N * M // 2
print(result)