import sys
import math
input = sys.stdin.readline

T = int(input().rstrip())

def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
        
for _ in range(T):
    n = int(input().rstrip())
    while True:
        if prime(n):
            print(n)
            break
        else:
            n += 1