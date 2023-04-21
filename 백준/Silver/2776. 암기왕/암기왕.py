import sys
input = sys.stdin.readline
t = int(input().rstrip())

def binary_search(data, target, start, end):
    if start > end:
        return 0
    else:
        mid = (start + end) // 2
        if target == data[mid]:
            return 1
        elif target > data[mid]:
            return binary_search(data, target, mid + 1, end)
        else:
            return binary_search(data, target, start, mid - 1)

for _ in range(t):
    n = int(input().rstrip())
    data = list(map(int, input().rstrip().split()))
    data.sort()
    m = int(input().rstrip())
    target_list = list(map(int, input().rstrip().split()))
    for i in target_list:
        print(binary_search(data, i, 0, n - 1))
