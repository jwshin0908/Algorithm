import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = []

for _ in range(n):
    array.append(input().rstrip())

result = list(set(array))
result = sorted(result, key=lambda x: (len(x), x))

for i in result:
    print(i)
