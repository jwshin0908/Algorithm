import sys

input = sys.stdin.readline
n = int(input().rstrip())
array = []

for _ in range(n):
    array.append(list(map(int, input().rstrip().split())))

# 결과 저장용 DP 테이블
d = [[0] * i for i in range(1, n + 1)]

# 다이나믹 프로그래밍(Bottom-Up 방식)
d[0][0] = array[0][0]

for i in range(1, n):
    for j in range(i + 1):
        # 바로 위층 더하기
        if j == 0:
            d[i][j] = d[i - 1][j] + array[i][j]
        # 위층의 마지막 값 더하기
        elif j == i:
            d[i][j] = d[i - 1][j - 1] + array[i][j]
        # 위층의 왼쪽 또는 바로 위쪽 중에 최댓값과 더하기
        else:
            d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + array[i][j]
print(max(d[n - 1]))