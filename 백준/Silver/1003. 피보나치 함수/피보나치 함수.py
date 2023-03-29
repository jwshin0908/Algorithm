import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())

    # 결과 저장용 DP 테이블
    d = [0] * 41
    d[0] = [1, 0]
    d[1] = [0, 1]

    # 다이나믹 프로그래밍(Bottom-Up 방식)
    for i in range(2, n + 1):
        d[i] = [d[i - 2][0] + d[i - 1][0], d[i - 2][1] + d[i - 1][1]]

    print(' '.join(map(str, d[n])))