import sys
input = sys.stdin.readline

list1 = list(input().rstrip())
list2 = list(input().rstrip())
list3 = list(input().rstrip())
list4 = list(input().rstrip())
list5 = list(input().rstrip())

list_all = [list1, list2, list3, list4, list5]
max_len = max(len(list1), len(list2), len(list3), len(list4), len(list5))

for i in range(max_len):
    for j in list_all:
        if len(j) - 1 < i:
            continue
        print(j[i], end='')