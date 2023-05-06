import sys

n = int(sys.stdin.readline().rstrip())
cnt = 0

if n < 100:
    cnt = n
    print(cnt)
else:
    for i in range(100, n + 1):
        num = str(i)
        if (int(num[2]) - int(num[1])) == (int(num[1]) - int(num[0])):
            cnt += 1
    print(99 + cnt)