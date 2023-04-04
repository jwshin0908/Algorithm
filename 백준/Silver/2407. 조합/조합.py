# itertools.combinations() 사용 시 시간 초과
# math.factorial() 을 이용해 직접 구현

import math
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

def combination(x, y):
    a = math.factorial(y) * math.factorial(x - y)
    return math.factorial(x) // a

result = combination(n, m)
print(result)