import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    array = {}
    for _ in range(n):
        value, key = input().rstrip().split()
        if key not in array.keys():
            array[key] = 1
        else:
            array[key] += 1
    result = 1
    for i in array.keys():
        result *= (array[i] + 1)
    print(result - 1)