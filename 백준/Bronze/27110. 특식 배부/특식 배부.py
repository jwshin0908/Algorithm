import sys
input = sys.stdin.readline

N = int(input().rstrip())
A, B, C = map(int, input().rstrip().split())
result = min(N, A) + min(N, B) + min(N, C)

print(result)