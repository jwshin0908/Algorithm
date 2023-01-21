# Q04. 만들 수 없는 금액(p.314)
# 해설 참고(p.512)

N = int(input())
data = list(map(int, input().split()))
data.sort()

result = 1 # 최솟값 1부터 시작

for i in data:
  if result < i: # 최솟값이 data에 있는 어떠한 값보다 작을 경우
    break # 해당 최솟값을 만들 방법 X -> break
  else:
    result += i

print(result)