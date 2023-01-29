# 오래걸리는 거부터 앞에 배치(그중에서 max가 결과값)

import sys
n = int(sys.stdin.readline().rstrip())
days = list(map(int, sys.stdin.readline().rstrip().split()))

days.sort()
result = []

for i in days:
    result.append(i+n+1)
    n-=1
print(max(result))