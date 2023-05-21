import sys
n = list(sys.stdin.readline().rstrip())

nums = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}

for i in n:
    if i in ['6', '9']:
        nums['6'] += 1
    else:
        nums[i] += 1

if nums['6'] % 2 == 0:
    nums['6'] = nums['6'] // 2
else:
    nums['6'] = nums['6'] // 2 + 1

print(max(nums.values()))