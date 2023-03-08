import sys

input = sys.stdin.readline

n = int(input().rstrip())
array = []

for _ in range(n):
    a, b = input().rstrip().split()
    array.append((int(a), b))

result = sorted(array, key=lambda x: x[0])

for i in result:
    print(' '.join(map(str, i)))
