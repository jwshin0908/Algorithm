import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    H, W, N = map(int, input().rstrip().split())
    floor = N % H
    room = N // H + 1
    if floor == 0:
        floor = H
        room -= 1
    print(floor * 100 + room)