# 6-4. 퀵 정렬 소스코드(p.168)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 왼쪽에서부터 피벗보다 큰 데이터 찾고, 오른쪽에서부터 피벗보다 작은 데이터 찾음
# 큰 데이터와 작은 데이터 위치를 서로 교환해줌
# 엇갈린 경우에는 작은 데이터와 피벗의 위치를 교환
def quick_sort(array, start, end):
  # 원소가 1개인 경우 종료
  if start >= end:
    return
  # pivot : 첫 번째 원소
  pivot = start
  # left : 첫 번째 원소(pivot) 제외 가장 왼쪽 원소
  left = start + 1
  # right : 가장 오른쪽 원소
  right = end
  while left <= right:
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while right > start and array[right] >= array[pivot]:
      right -= 1
    # 서로 엇갈렸다면 작은 데이터와 피벗을 교체
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    # 서로 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
    else:
      array[left], array[right] = array[right], array[left]
  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)