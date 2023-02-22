# 6-10. 위에서 아래로(p.178)

n = int(input())
array = []

for _ in range(n):
  array.append(int(input()))

array.sort(reverse=True)
print(' '.join(map(str, array)))