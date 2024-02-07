import sys
input = sys.stdin.readline

n = int(input().rstrip())
result = 0

for _ in range(n):
    result += int(input().rstrip())
    
print(result)