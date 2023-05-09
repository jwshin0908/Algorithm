import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
apples = []
for _ in range(int(input().rstrip())):
    apples.append(int(input().rstrip()))

loc = 1
result = 0
for apple in apples:
    # 가만히 있을 경우
    if (loc <= apple) and ((loc + m - 1) >= apple):
        pass
    # 좌측으로 이동할 경우
    elif loc > apple:
        result += abs(loc - apple)
        loc = apple
    # 우측으로 이동할 경우
    else:
        result += abs(apple - (loc + m - 1))
        loc = apple - m + 1

print(result)