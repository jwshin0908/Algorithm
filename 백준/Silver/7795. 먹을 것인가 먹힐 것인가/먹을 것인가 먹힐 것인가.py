import sys
input = sys.stdin.readline

T = int(input().rstrip())

def binary_search(target, array):
    start, end = 0, len(array) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

for _ in range(T):
    N, M = map(int, input().rstrip().split())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))
    A.sort()
    B.sort()
    cnt = 0
    for i in A:
        cnt += (binary_search(i, B) + 1)
    print(cnt)