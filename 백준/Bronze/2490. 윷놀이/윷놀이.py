import sys
input = sys.stdin.readline

result = {0 : 'E', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D'}

for _ in range(3):
    array = list(map(int, input().rstrip().split()))
    cnt = array.count(0)
    print(result[cnt])