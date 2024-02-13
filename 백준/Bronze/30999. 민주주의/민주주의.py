import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
cnt = 0

for _ in range(N):
    array = list(input().rstrip())
    if array.count('O') > array.count('X'):
        cnt += 1
        
print(cnt)