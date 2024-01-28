import sys
input = sys.stdin.readline

N = int(input().rstrip())
result = 1

for i in range(N):
    result *= (i + 1)
    
print(result)