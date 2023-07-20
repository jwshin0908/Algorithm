import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
array.sort()

start, end = 0, N - 1
cnt = 0

while start < end:
    if array[start] + array[end] > M:
        end -= 1
    elif array[start] + array[end] < M:
        start += 1
    else:
        cnt += 1
        end -= 1
        
print(cnt)