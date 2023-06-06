import sys
input = sys.stdin.readline

n = int(input())
array = []
result = []

for _ in range(n):
    array.append(list(map(int, input().rstrip().split())))

for i in range(n):
    cnt = 0
    for j in range(n):
        if (array[i][0] < array[j][0]) and (array[i][1] < array[j][1]):
            cnt += 1
    result.append(cnt + 1)

print(' '.join(map(str, result)))