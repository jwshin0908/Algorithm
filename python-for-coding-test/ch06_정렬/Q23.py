# Q23. 국영수(p.359)

n = int(input())
array = []

for _ in range(n):
  data = input().split()
  array.append([data[0], int(data[1]), int(data[2]), int(data[3])])

# 내림차순일 경우 key에서 -를 붙임
result = sorted(array, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in result:
  print(i[0])