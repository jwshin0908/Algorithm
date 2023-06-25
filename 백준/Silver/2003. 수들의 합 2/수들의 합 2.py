import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

start, end = 0, 1
cnt = 0

while (start <= end) and (end <= n):
    result = sum(array[start:end])
    if result == m:
        cnt += 1
        end += 1
    elif result > m:
        start += 1
    else:
        end += 1

print(cnt)