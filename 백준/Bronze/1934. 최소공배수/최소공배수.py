# 유클리드 호제법 : (a, b)의 최대공약수 = (b, a를 b로 나눈 나머지)의 최대공약수

import sys
input = sys.stdin.readline

t = int(input().rstrip())

def GCD(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def LCM(x, y):
    return x * y / GCD(x, y)


for _ in range(t):
    a, b = map(int, input().rstrip().split())
    print(int(LCM(a, b)))