import sys
while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == b == c == 0:
        break
    else:
        data = [a, b, c]
        data.sort()
        if data[0]**2 + data[1]**2 == data[2]**2:
            print('right')
        else:
            print('wrong')
