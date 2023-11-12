import sys
input = sys.stdin.readline

max_chef = 0
max_score = 0

for i in range(5):
    array = list(map(int, input().rstrip().split()))
    if sum(array) > max_score:
        max_chef = i + 1
        max_score = sum(array)
print(max_chef)
print(max_score)