import math
import sys
input = sys.stdin.readline

M = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
K = int(input().rstrip())

array_sum = sum(array)
all_combin = math.comb(array_sum, K)
cnt = 0

for i in array:
    cnt += math.comb(i, K)

print(cnt / all_combin)