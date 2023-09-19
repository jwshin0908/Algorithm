import sys
input = sys.stdin.readline

result = []
cnt = 0
for _ in range(4):
    a, b = map(int, input().rstrip().split())
    cnt += (b - a)
    result.append(cnt)
    
print(max(result))