import sys
input = sys.stdin.readline

x = input().rstrip()
cnt = 0

while True:
    if len(x) == 1:
        break
    x = str(sum([int(i) for i in str(x)]))
    cnt += 1

print(cnt)
if int(x) % 3 == 0:
    print('YES')
else:
    print('NO')