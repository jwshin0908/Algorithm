# 6-1. 선택 정렬 소스코드(p.159)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  # 가장 작은 원소의 index
  min_index = i
  for j in range(i + 1, len(array)):
    # 현재 가장 작은 원소보다 더 작은 원소가 있다면
    if array[min_index] > array[j]:
      # 해당 위치를 index로 담음
      min_index = j
  # 가장 작은 원소와 가장 앞쪽 원소를 바꿈
  array[i], array[min_index] = array[min_index], array[i]

print(array)
