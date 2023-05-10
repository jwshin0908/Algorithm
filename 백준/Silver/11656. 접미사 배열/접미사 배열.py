import sys

x = sys.stdin.readline().rstrip()
array = []

for i in range(len(x)):
    array.append(x[i:])

array.sort()

for j in array:
    print(j)