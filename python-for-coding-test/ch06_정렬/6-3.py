# 6-3. 삽입 정렬 소스코드(p.164)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  # index i부터 1까지 감소하면서 반복
  for j in range(i, 0, -1):
    # 한 칸씩 왼쪽으로 이동
    if array[j] < array[j - 1]:
      # 자신이 더 작다면 swap 수행
      array[j], array[j - 1] = array[j - 1], array[j]
    # 자신보다 작은 원소를 만날 경우 그 위치에서 멈춤
    else:
      break

print(array)