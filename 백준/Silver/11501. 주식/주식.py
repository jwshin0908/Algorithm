import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    price = list(map(int, input().rstrip().split()))
    result = 0
    max_value = 0
    for i in range(N - 1, -1, -1):
        if price[i] > max_value:
            max_value = price[i]
        else:
            result += max_value - price[i]
    print(result)