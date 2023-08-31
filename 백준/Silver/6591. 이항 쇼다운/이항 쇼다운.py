import math
import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().rstrip().split())
    if (n == 0) and (k == 0):
        break
    result = math.comb(n, k)
    print(result)