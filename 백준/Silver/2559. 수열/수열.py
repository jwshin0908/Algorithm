import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

num = sum(array[:K])
result = num

for i in range(N - K):
    num += (array[K + i] - array[i])
    if result < num:
        result = num
        
print(result)