import sys
input = sys.stdin.readline

n = input().rstrip()
nums = list(map(int, input().rstrip().split()))

nums = list(set(nums))

nums.sort()

print(" ".join(map(str, nums)))