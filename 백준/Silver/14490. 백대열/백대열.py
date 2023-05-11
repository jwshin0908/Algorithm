import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split(':'))


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


result = gcd(n, m)

new_n = int(n // result)
new_m = int(m // result)

print(f"{new_n}:{new_m}")