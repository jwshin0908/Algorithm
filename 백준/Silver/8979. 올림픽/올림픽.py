import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().rstrip().split())))

array.sort(key = lambda x : (-x[1], -x[2], -x[3]))

for i in range(N):
    if array[i][0] == K:
        result = i

# 공동 등수인 경우
for j in range(N):
    if array[j][1:] == array[result][1:]:
        print(j + 1)
        break