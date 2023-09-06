import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
d = [0] * n
d[0] = array[0]

for i in range(1, n):
    d[i] = max(array[i], d[i - 1] + array[i])
    
print(max(d))