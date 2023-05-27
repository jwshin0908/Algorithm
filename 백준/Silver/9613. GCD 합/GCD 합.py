import sys
input = sys.stdin.readline

t = int(input().rstrip())


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for _ in range(t):
    array = list(map(int, input().rstrip().split()))
    gcd_list = []
    for i in range(1, array[0] + 1):
        for j in range(i + 1, array[0] + 1):
            gcd_list.append(gcd(array[i], array[j]))
    print(sum(gcd_list))