import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = []

for _ in range(n):
    array.append(list(input().rstrip().split()))

result = sorted(array, key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(result[-1][0])
print(result[0][0])