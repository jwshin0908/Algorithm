# Q07. 럭키 스트레이트(p.321)

N = str(input())
index = int(len(N) / 2)

left = N[:index]
right = N[index:]

left_sum = 0
right_sum = 0

for i in left:
  left_sum += int(i)

for j in right:
  right_sum += int(j)

if left_sum == right_sum:
  print('LUCKY')
else:
  print('READY')