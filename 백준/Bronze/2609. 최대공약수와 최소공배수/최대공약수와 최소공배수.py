# 유클리드 호재법 : a, b의 최대공약수와 b, r(a%b의 나머지)의 최대공약수가 같다
a, b = map(int, input().split())

def GCD(x, y):
  while y > 0:
    x, y = y, x % y
  return x

# 최소공배수(LCM) : a, b의 곱을 최대공약수(GCD)로 나눈 몫
def LCM(x, y):
  return int(x * y / GCD(x, y))

print(GCD(a, b))
print(LCM(a, b))