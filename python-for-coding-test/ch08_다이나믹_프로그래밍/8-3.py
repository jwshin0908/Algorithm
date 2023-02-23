# 8-3. 호출되는 함수 확인(p.214)

# 탑다운 방식(Top-Down)
# 한 번 계산된 결과 -> 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
  print('f(' + str(x) + ')', end=' ')
  # 종료 조건(1 or 2일 때 1을 반환)
  if x == 1 or x == 2:
    return 1
  # 이미 계산된 문제라면 그대로 반환
  if d[x] != 0:
    return d[x]
  # 이미 계산되지 않은 문제라면 점화식에 따라 피보나치 결과 반환
  d[x] = fibo(x - 1) + fibo(x - 2)
  return d[x]

fibo(6)