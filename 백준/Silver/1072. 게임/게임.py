# 풀이 참고
import sys
input = sys.stdin.readline

x, y = map(int, input().rstrip().split())
z = 100 * y // x

if z >= 99:
    print(-1)
else:
    result = 0
    start = 1
    end = x

    while start <= end:
        mid = (start + end) // 2
        if 100 * (y + mid) // (x + mid) <= z:
            start = mid + 1
        else:
            result = mid
            end = mid - 1
    print(result)