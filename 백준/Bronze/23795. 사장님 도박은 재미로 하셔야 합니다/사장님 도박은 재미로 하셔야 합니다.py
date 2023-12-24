import sys
input = sys.stdin.readline
cnt = 0

while True:
    n = int(input().rstrip())
    if n == -1:
        break
    else:
        cnt += n

print(cnt)