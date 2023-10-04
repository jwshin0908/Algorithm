import sys
input = sys.stdin.readline

n = int(input().rstrip())
result = 1

for i in range(1, n + 1):
    result *= i

print(result)