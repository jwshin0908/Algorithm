# 3-4. 1이 될 때까지(p.99)

N, K = map(int, input().split())

cnt = 0

while True:
  if N < K : # N이 K보다 작을 때 나눌 수 없음
    cnt+=(N-1) # 1이 될 때까지 빼는 횟수 cnt에 더하기
    break # 반복문 탈출
    
  elif N%K == 0 : # N이 K의 배수인 경우
    cnt+=1 # 한 번 나누었으므로 cnt에 1 추가
    N = N//K # N은 K로 나눈 몫
    
  else : # N이 K의 배수가 아닌 경우
    cnt+=N%K # 나머지를 제거하는 만큼 cnt에 추가
    N = N//K # N은 K로 나눈 몫

print(cnt)