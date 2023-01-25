# 4-2. 시각(p.113)
# 완전 탐색(Brute Forcing) 유형

N = int(input())
cnt = 0

# hour, minute, second에 대한 3중 for문 수행
for h in range(0, N + 1):
  for m in range(60):
    for s in range(60):
      # h, m, s를 string 형태로 모두 더한 시각에 '3'이 포함되면 cnt 1 증가
      if '3' in str(h) + str(m) + str(s):
        cnt += 1

print(cnt)