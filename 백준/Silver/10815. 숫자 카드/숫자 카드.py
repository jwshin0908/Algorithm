import sys
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

# 이진 탐색은 정렬이 되어있어야 사용 가능
array.sort()

# 이진 탐색 반복문 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        # 중간점 값보다 target이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid-1
        # 중간점 값보다 target이 큰 경우 오른쪽 확인
        else:
            start = mid+1
    return None

# target 값을 nums에서 돌아가면서 확인
for i in nums:
    target = i
    result = binary_search(array, target, 0, n-1)
    if result == None:
        print(0, end=' ')
    else:
        print(1, end=' ')