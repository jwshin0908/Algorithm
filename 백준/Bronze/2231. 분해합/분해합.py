import sys
input = sys.stdin.readline
n = int(input())
array = []

for i in range(1, n):
    nums = list(map(int, str(i)))
    if i + sum(nums) == n:
        array.append(i)

if len(array) != 0:
    print(array[0])
else:
    print(0)