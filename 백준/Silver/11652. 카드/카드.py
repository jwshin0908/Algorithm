import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = dict()

for _ in range(N):
    x = int(input().rstrip())
    if x not in nums.keys():
        nums[x] = 1
    else:
        nums[x] += 1
        
result = sorted(nums.items(), key=lambda x: (-x[1], x[0]))

print(result[0][0])