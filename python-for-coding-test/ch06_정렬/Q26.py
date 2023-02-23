# Q26. 카드 정렬하기(p.363)
# sort를 사용할 경우 시간 초과 발생

import sys
import heapq

n = int(sys.stdin.readline().rstrip())

heap = []
for _ in range(n):
  data = int(sys.stdin.readline().rstrip())
  heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
  first = heapq.heappop(heap)
  second = heapq.heappop(heap)
  sum = first + second
  result += sum
  heapq.heappush(heap, sum)

print(result)


# 시간 초과 코드
'''
import sys

n = int(sys.stdin.readline().rstrip())
card = []
sum = 0

for _ in range(n):
    card.append(int(sys.stdin.readline().rstrip()))

card.sort()
result = 0

if len(card) == 1:
    print(card)

# card 리스트 갱신, result에 누적합 더하기
while True:
    if len(card) == 1:
        break
    sum = card[0] + card[1]
    result += sum
    card = card[2:]
    card.append(sum)
    card.sort()
    
print(result)
'''