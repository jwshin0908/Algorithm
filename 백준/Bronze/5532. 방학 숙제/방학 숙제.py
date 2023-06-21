import sys
import math
input = sys.stdin.readline

l = int(input().rstrip())
a = int(input().rstrip())
b = int(input().rstrip())
c = int(input().rstrip())
d = int(input().rstrip())

e = a // c
f = b // d

if e > f:
    if a % c == 0:
        print(l - e)
    else:
        print(l - 1 - e)
else:
    if b % d == 0:
        print(l - f)
    else:
        print(l - 1 - f)