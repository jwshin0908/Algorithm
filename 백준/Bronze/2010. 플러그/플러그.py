import sys
input = sys.stdin.readline

N = int(input().rstrip())
cnt = 0

for _ in range(N):
    n = int(input().rstrip())
    cnt += n

print(cnt - N + 1)