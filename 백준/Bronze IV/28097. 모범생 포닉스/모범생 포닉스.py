import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = list(map(int, input().rstrip().split()))

time = (N - 1) * 8 + sum(array)

day = time // 24
hour = time % 24

print(day, hour)