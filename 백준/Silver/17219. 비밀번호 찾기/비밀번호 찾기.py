import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

dict = {}

for _ in range(n):
    x, y = input().rstrip().split()
    dict[x] = y

for i in range(m):
    z = input().rstrip()
    print(dict[z])