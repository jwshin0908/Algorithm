import sys

n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
m = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

array.sort()

def binary_search(array, target, start, end):
    if start > end:
        print(0)
    else:
        mid = (start + end) // 2
        if target == array[mid]:
            print(1)
        elif target > array[mid]:
            return binary_search(array, target, mid + 1, end)
        else:
            return binary_search(array, target, start, mid - 1)

for i in nums:
    binary_search(array, i, 0, n - 1)
