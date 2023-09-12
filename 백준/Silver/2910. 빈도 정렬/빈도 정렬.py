import sys
input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))
nums_dict = {}
idx = 1
for i in array:
    if i not in nums_dict:
        nums_dict[i] = 1
    else:
        nums_dict[i] += 1

nums_dict = sorted(nums_dict.items(), key=lambda x: -x[1])

for key, value in nums_dict:
    for _ in range(value):
        print(key, end=' ')