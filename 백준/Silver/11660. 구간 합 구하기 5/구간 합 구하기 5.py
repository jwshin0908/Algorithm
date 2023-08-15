import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().rstrip().split())))

d = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        d[i][j] = d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1] + array[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    result = d[x2][y2] - d[x2][y1 - 1] - d[x1 - 1][y2] + d[x1 - 1][y1 - 1]
    print(result)