# 1. 첫 번째 값 기준 오름차순 정렬
# 2. 반복문으로 해당 값 아래의 값들에 대해 2번째 값 min value update(맞으면 살아남음)
# 1 4
# 2 3
# 3 2
# 4 1
# 5 5

import sys
input = sys.stdin.readline
t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    array = []
    cnt = 1
    
    for _ in range(n):
        array.append(list(map(int, input().rstrip().split())))
        
    array.sort(key=lambda x: x[0])
    min_value = array[0][1]
    
    for i in range(1, n):
        if array[i][1] < min_value:
            min_value = array[i][1]
            cnt += 1
    print(cnt)