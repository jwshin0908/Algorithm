# 6-11. 성적이 낮은 순서로 학생 출력하기(p.180)

n = int(input())
array = []

for _ in range(n):
  data = input().split()
  array.append([data[0], int(data[1])])

result = sorted(array, key=lambda x: x[1])

for i in result:
  print(i[0], end=' ')