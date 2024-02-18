import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    a, b, c = map(int, input().rstrip().split())
    cnt = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                if (i % j == j % k) and (i % j == k % i):
                    cnt += 1
    print(cnt)