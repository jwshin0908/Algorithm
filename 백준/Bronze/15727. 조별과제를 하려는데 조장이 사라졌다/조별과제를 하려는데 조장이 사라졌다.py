import sys
input = sys.stdin.readline

t = int(input().rstrip())
cnt = 0

while True:
    if cnt * 5 >= t:
        break
    else:
        cnt += 1

print(cnt)