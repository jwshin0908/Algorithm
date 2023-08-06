import sys
input = sys.stdin.readline

T = int(input().rstrip())

def check(x1, y1, x2, y2, cx, cy, r):
    case1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
    case2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
    if (case1 < r ** 2) and (case2 < r ** 2):
        return 0
    elif case1 < r ** 2:
        return 1
    elif case2 < r ** 2:
        return 1
    else:
        return 0

for _ in range(T):
    result = 0
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    n = int(input().rstrip())
    for _ in range(n):
        cx, cy, r = map(int, input().rstrip().split())
        result += check(x1, y1, x2, y2, cx, cy, r)
    print(result)