import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
array = []

for _ in range(n):
    P, L = map(int, input().rstrip().split())
    mileages = list(map(int, input().rstrip().split()))
    if P < L:
        array.append(1)
    else:
        mileages.sort(reverse = True)
        array.append(mileages[L - 1])
    
array.sort()
cnt = 0

for i in array:
    m -= i
    cnt += 1
    if m < 0:
        print(cnt - 1)
        break
if m > 0:
    print(cnt)