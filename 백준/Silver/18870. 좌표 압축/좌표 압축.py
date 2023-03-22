# list.index(i)를 사용할 경우 시간 초과 발생
# dictionary 사용해 index를 저장

import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

array = sorted(list(set(nums)))

nums_dict = {array[i]: i for i in range(len(array))}

for i in nums:
    print(nums_dict[i], end=' ')
