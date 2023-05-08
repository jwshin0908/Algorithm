import sys

input = sys.stdin.readline
a, b = map(int, input().rstrip().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

print(int(lcm(a, b)))