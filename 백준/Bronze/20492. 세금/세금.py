import sys
input = sys.stdin.readline

N = int(input().rstrip())
result1 = int(0.78 * N)
result2 = int(0.8 * N + 0.2 * 0.78 * N)

print(result1, result2)