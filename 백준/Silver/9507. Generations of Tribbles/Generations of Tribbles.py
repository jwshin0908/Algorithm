import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    
    # 결과 저장용 DP 테이블
    d = [0] * 68

    d[0] = 1
    d[1] = 1
    d[2] = 2
    d[3] = 4

    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3] + d[i - 4]

    print(d[n])