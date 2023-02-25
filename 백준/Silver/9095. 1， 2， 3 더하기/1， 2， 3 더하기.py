t = int(input())

for _ in range(t):
    n = int(input())
    # 결과 저장용 DP 테이블
    d = [0] * 11
    # 다이나믹 프로그래밍(Bottom-Up 방식)
    d[1] = 1
    d[2] = 2
    d[3] = 4
    # i의 경우는 (i-1), (i-2), (i-3) 경우의 합
    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    print(d[n])