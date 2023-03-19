n = int(input())

# 결과 저장용 DP 테이블
d = [0] * 501

# 다이나믹 프로그래밍(Bottom-Up 방식)
d[0] = 1
d[1] = 1

for i in range(2, n + 1):
    d[i] = i * d[i - 1]

x = d[n]
cnt = 0

while True:
    if x % 10 == 0:
        cnt += 1
        x = int(x // 10)
    else:
        break
        
print(cnt)