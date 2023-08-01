import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
m = int(input().rstrip())

prefix = [0] * n
prefix[0] = array[0]

for i in range(1, n):
    prefix[i] = prefix[i - 1] + array[i]

for _ in range(m):
    i, j = list(map(int, input().rstrip().split()))
    if i == 1:
        print(prefix[j - 1])
    else:
        print(prefix[j - 1] - prefix[i - 2])