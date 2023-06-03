import sys
n = int(sys.stdin.readline().rstrip())

length = len(str(n))
cnt = 0

for i in range(1, length):
    cnt += i * (9 * 10**(i - 1))

cnt += length * (n - 10**(length - 1) + 1)

print(cnt)