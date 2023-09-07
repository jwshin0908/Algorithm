import sys
input = sys.stdin.readline

N, L = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))
cnt = 1
array.sort()

start = array[0] - 0.5
end = start + L

for i in range(1, len(array)):
    if (start <= array[i]) and (array[i] <= end):
        continue
    else:
        cnt += 1
        start = array[i] - 0.5
        end = start + L

print(cnt)