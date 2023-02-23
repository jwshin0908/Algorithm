# 8-1. 피보나치 함수 소스코드(p.210)

# 피보나치 함수를 재귀 함수로 표현
def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x - 1) + fibo(x - 2)

print(fibo(4))