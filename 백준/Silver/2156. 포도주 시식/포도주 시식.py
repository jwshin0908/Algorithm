import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = [0] * 10002
for i in range(1, n + 1):
    array[i] = int(input().rstrip())

# 결과 저장용 DP 테이블
d = [0] * 10002

d[1] = array[1]
d[2] = array[1] + array[2]

# 현재 위치 O, 바로 전 와인을 O : -3 위치의 최댓값에서 하나 건너 뛴 경우
# 현재 위치 O, 이전 와인이 건너 뛴 와인 : -2 위치의 최댓값을 더한 경우
# 현재 위치 X, -1 위치의 최댓값 : 현재 위치의 최댓값
for i in range(3, n + 1):
    d[i] = max(d[i - 1], d[i - 2] + array[i], d[i - 3] + array[i - 1] + array[i])

print(d[n])