import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
sorted_array = sorted(array)
result = [0] * N

for i in range(N):
    idx = sorted_array.index(array[i])
    result[i] = idx
    sorted_array[idx] = -1
    
print(*result)    