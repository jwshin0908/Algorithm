import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))

# 결과 저장용 DP 테이블
d_up = [1] * (n + 1)
d_down = [1] * (n + 1)

for i in range(1, n):
    if array[i] >= array[i - 1]:
        d_up[i] = d_up[i - 1] + 1

    if array[i] <= array[i - 1]:
        d_down[i] = d_down[i - 1] + 1

print(max(max(d_up), max(d_down)))