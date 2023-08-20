import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = []
distance = []
for _ in range(N):
    array.append(list(map(int, input().rstrip().split())))
    
for i in range(N - 1):
    cnt = (abs(array[i + 1][0] - array[i][0]) + abs(array[i + 1][1] - array[i][1]))
    distance.append(cnt)

total_dist = sum(distance)
min_dist = total_dist

for i in range(1, N - 1):
    dist = total_dist - distance[i - 1] - distance[i] + (abs(array[i + 1][0] - array[i - 1][0]) + abs(array[i + 1][1] - array[i - 1][1]))
    min_dist = min(min_dist, dist)

print(min_dist)