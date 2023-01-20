# Q02. 곱하기 혹은 더하기(p.312)

nums = list(map(int, input()))

result = 0

for i in nums:
  if result * i <= result:  # result에 i를 곱했는데 작아지거나 그대로인 경우
    result += i  # 더하기를 수행
  else:  # 곱하기 수행
    result *= i

print(result)
