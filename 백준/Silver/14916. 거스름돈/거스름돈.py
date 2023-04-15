import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
while n >= 0:
    if n % 5 == 0:
        cnt += (n // 5)
        print(cnt)
        break
    else:
        n -= 2
        cnt += 1
else:
    print(-1)
