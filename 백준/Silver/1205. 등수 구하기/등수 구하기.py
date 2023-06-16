import sys
input = sys.stdin.readline

n, score, p = map(int, input().rstrip().split())
if n > 0:
    array = list(map(int, input().rstrip().split()))
else:
    array = []

if n < p:
    array.append(score)
    array.sort(reverse=True)
    print(1 + array.index(score))
else:
    if score <= array[-1]:
        print(-1)
    else:
        array.append(score)
        array.sort(reverse=True)
        print(1 + array.index(score))