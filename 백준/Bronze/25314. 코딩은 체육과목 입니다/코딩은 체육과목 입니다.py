import sys
input = sys.stdin.readline

N = int(input().rstrip())
cnt = N // 4

for _ in range(cnt):
    print('long', end = ' ')
print('int')