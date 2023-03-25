import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    x = int(input().rstrip())

    # 결과 저장용 DP 테이블
    d = [0] * 101

    # 다이나믹 프로그래밍(Bottom-Up 방식)
    d[0] = 0
    d[1] = 1
    d[2] = 1
    d[3] = 1
    d[4] = 2
    
    for i in range(5, x + 1):
        d[i] = d[i - 5] + d[i - 1]
        
    print(d[x])