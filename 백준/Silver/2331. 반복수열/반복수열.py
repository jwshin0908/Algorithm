import sys
input = sys.stdin.readline

A, P = map(int, input().rstrip().split())
array = [A]

while True:
    num_split = list(str(array[-1]))
    num = sum([int(i) ** P for i in num_split])
    array.append(num)
    if len(array) != len(set(array)):
        break

for i in array:
    if array.count(i) == 2:
        loc = array.index(i)
print(loc)