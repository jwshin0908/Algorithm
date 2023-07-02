import sys
input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

start, end = 0, 0
temp_sum = array[0]
length = 100001

while True:
    if temp_sum >= S:
        length = min(length, end - start + 1)
        temp_sum -= array[start]
        start += 1
    else:
        end += 1
        if end == N:
            break
        temp_sum += array[end]
        
if length == 100001:
    print(0)
else:
    print(length)