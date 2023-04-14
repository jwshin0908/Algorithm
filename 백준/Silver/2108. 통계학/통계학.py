import sys

input = sys.stdin.readline

n = int(input().rstrip())
array = []

for _ in range(n):
    array.append(int(input().rstrip()))

array.sort()
array_mean = round(sum(array) / n)
array_median = array[(n - 1) // 2]

array_dict = {}

for i in array:
    if i in array_dict:
        array_dict[i] += 1
    else:
        array_dict[i] = 1
    
max_count = max(array_dict.values())
array_new = []

for key in array_dict:
    if array_dict[key] == max_count:
        array_new.append(key)

if len(array_new) == 1:
    array_mode = array_new[0]
else:
    array_mode = array_new[1]
array_range = array[-1] - array[0]

print(array_mean)
print(array_median)
print(array_mode)
print(array_range)