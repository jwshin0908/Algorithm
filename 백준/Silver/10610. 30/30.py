import sys
input = sys.stdin.readline

n = list(input().rstrip())
array = [int(i) for i in n]

array.sort(reverse=True)
a = sum(array)
if array[-1] == 0:
    if a % 3 == 0:
        print(''.join(map(str, array)))
    else:
        print(-1)
else:
    print(-1)
