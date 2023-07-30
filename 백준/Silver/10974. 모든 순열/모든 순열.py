from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = [i for i in range(1, N + 1)]

data = permutations(nums, N)

for i in data:
    print(' '.join(map(str, i)))