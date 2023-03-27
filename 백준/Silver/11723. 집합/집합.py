# set.remove() : 제거하려는 값이 존잰하지 않으면 KeyError가 발생
# set.discard() : 값이 없어도 정상종료

import sys

input = sys.stdin.readline

m = int(input().rstrip())
s = set()

for _ in range(m):
    order = sys.stdin.readline().rstrip().split()
    if len(order) == 1:
        if order[0] == "all":
            s = set([i for i in range(1, 21)])
        elif order[0] == 'empty':
            s = set()
    else:
        func, x = order[0], order[1]
        x = int(x)
        if func == "add":
            s.add(x)
        elif func == "remove":
            s.discard(x)
        elif func == "check":
            print(1 if x in s else 0)
        elif func == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)