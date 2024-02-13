import sys
input = sys.stdin.readline

N = int(input().rstrip())
result = 1

if N > 10:
    for i in range(11, N + 1):
        result *= i
        
print(6 * result)