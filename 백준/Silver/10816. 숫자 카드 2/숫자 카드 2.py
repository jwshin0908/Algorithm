import sys

input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().rstrip().split()))
m = int(input())
find = list(map(int, input().rstrip().split()))

cards.sort()
cards_dict = {}

# 주어진 숫자 카드의 카드 종류별 개수 dictionary 지정
for i in cards:
    if i in cards_dict:
        cards_dict[i] += 1
    else:
        cards_dict[i] = 1

# binary search를 통해 존재한다면 dictionary에서 target 카드의 개수 return
def binary_search(data, target, start, end):
    if start > end:
        return 0
    else:
        mid = (start + end) // 2
        if data[mid] == target:
            return cards_dict[target]
        elif data[mid] > target:
            return binary_search(data, target, start, mid - 1)
        else:
            return binary_search(data, target, mid + 1, end)

for j in find:
    print(binary_search(cards, j, 0, n - 1), end=' ')