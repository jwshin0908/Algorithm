import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c, d = map(int, input().rstrip().split())

x = a * d + b * c
y = b * d


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

xy_gcd = gcd(x, y)

print(int(x / xy_gcd), int(y / xy_gcd))