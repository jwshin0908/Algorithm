# 일반적인 방법으로는 시간 초과 발생
import sys
import math
m, n  = map(int, sys.stdin.readline().rstrip().split())

for i in range(m, n+1):
    condition = True
    if i<=1:
        continue
    for j in range(2, int(math.sqrt(i))+1):
        if i%j==0:
            condition = False
            break
    if condition:
        print(i)