# B -> A 방향으로 해결
# B를 10으로 나눈 나머지가 1인 경우 & 2로 나눈 나머지가 0인 경우

import sys

input = sys.stdin.readline
a, b = map(int, input().rstrip().split())

cnt = 1

while True:
    if a == b :
        break
    elif a > b :
        cnt = -1
        break
    elif b % 10 == 1:
        b = b // 10
        cnt += 1
    elif b % 2 == 0:
        b = b // 2
        cnt += 1
    else:
        cnt = -1
        break
        
print(cnt)