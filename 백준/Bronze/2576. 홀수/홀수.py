import sys
input = sys.stdin.readline

array = [int(input().rstrip()) for _ in range(7)]
array.sort()

new_array = [i for i in array if i % 2 != 0]

if len(new_array) == 0:
    print(-1)
else:
    print(sum(new_array))
    print(new_array[0])