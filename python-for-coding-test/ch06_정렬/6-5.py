# 6-5. 파이썬의 장점을 살린 퀵 정렬 소스코드(p.169)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 왼쪽에서부터 피벗보다 큰 데이터 찾고, 오른쪽에서부터 피벗보다 작은 데이터 찾음
# 큰 데이터와 작은 데이터 위치를 서로 교환해줌
# 엇갈린 경우에는 작은 데이터와 피벗의 위치를 교환
def quick_sort(array):
  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array

  pivot = array[0]  # 피벗은 첫 번째 원소
  tail = array[1:]  # 피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

  # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))