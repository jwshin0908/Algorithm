import sys
n = int(sys.stdin.readline().rstrip())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))
    
nums.sort()

for i in nums:
    print(i)