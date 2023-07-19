import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
m = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
array = array[::-1]

num = 0
for i in range(m):
    num += array[i] * a ** i

result = []
while num != 0:
    result.append(num % b)
    num = num // b
result = result[::-1]

print(' '.join(map(str, result)))