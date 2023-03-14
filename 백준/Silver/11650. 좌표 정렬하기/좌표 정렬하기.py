import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = []

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    array.append([a, b])
    
result = sorted(array, key=lambda x:(x[0], x[1]))

for i in result:
    print(" ".join(map(str, i)))