import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

start, end = 0, max(array)

while start <= end:
    mid = (start + end) // 2
    cut_sum = 0
    for i in array:
        if i > mid:
            cut_sum += i - mid
    if cut_sum < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(end)