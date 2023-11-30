import sys
input = sys.stdin.readline

C, K, P = map(int, input().rstrip().split())
cnt = 0

for i in range(C + 1):
    cnt += K * i + P * i**2
    
print(cnt)