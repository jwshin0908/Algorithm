import sys
input = sys.stdin.readline

n = int(input().rstrip())

start, end = 0, n
while start <= end:
    mid = (start + end) // 2
    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1
        
print(start)