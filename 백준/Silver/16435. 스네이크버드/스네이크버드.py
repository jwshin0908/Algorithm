import sys
input = sys.stdin.readline

n, l = map(int, input().rstrip().split())
h = list(map(int, input().rstrip().split()))
h.sort()

while True:
    if h[0] <= l:
        l += 1
        if len(h) > 1:
            h = h[1:]
        else:
            print(l)
            break
    else:
        print(l)
        break