import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

array = [[1 for _ in range(i)] for i in range(1, 31)]

for i in range(2, 30):
    for j in range(1, i):
        array[i][j] = array[i - 1][j - 1] + array[i - 1][j]

print(array[n-1][k-1])