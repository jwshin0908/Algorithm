import sys
input = sys.stdin.readline

n = int(input().rstrip())
start, end = 0, 0
total = 0
cnt = 0

while end <= n:
    if total < n:
        end += 1
        total += end
    elif total > n:
        total -= start
        start += 1
    else:
        cnt += 1
        end += 1
        total += end
        
print(cnt)