import sys
input = sys.stdin.readline

n = int(input().rstrip())


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return int(x * y / gcd(x, y))

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    print(lcm(a, b))