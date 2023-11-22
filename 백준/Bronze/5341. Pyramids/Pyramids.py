import sys
input = sys.stdin.readline

while True:
    cnt = 0
    n = int(input().rstrip())
    if n == 0:
        break
    for i in range(n + 1):
        cnt += i
    print(cnt)