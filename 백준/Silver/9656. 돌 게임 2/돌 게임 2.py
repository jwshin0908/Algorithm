import sys
n = int(sys.stdin.readline().rstrip())

# 결과 저장용 DP 테이블
d = [0] * 1001

# 다이나믹 프로그래밍(Bottom-Up 방식)
d[0] = 0
d[1] = 0  # 창영 승리
d[2] = 1  # 상근 승리

# 돌의 개수가 홀수면 창영 승리, 짝수면 상근 승리
for i in range(3, n + 1):
    d[i] = 1 if i % 2 == 0 else 0
if d[n] == 1:
    print('SK')
else:
    print('CY')