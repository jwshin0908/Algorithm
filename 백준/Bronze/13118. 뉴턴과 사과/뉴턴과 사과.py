import sys
input = sys.stdin.readline

array = list(map(int, input().rstrip().split()))
x, y, r = map(int, input().rstrip().split())

if x in array:
    print(array.index(x) + 1)
else:
    print(0)