import sys
input = sys.stdin.readline

M = int(input().rstrip())
N = int(input().rstrip())
array = []

for i in range(int(M ** 0.5), int(N ** 0.5) + 1):
    if (i ** 2 >= M) and (i ** 2 <= N):
        array.append(i ** 2)

if len(array) == 0:
    print(-1)
else:
    print(sum(array))
    print(min(array))