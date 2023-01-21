# Q03. 문자열 뒤집기(p.313)

data = list(map(int, input()))  # 입력을 list 숫자 요소로 투입
cnt = 0  # 뒷자리와 숫자가 다른 횟수

for i in range(len(data) - 1):  # list을 순환하며 실행
  if data[i] != data[i + 1]:  # 뒷자리와 숫자가 서로 다를 경우
    cnt += 1

if cnt % 2 == 1:  # 짝수일 경우 1/2, 홀수일 경우 1/2의 올림값
  result = int((cnt + 1) / 2)
else:
  result = int(cnt / 2)

print(result)