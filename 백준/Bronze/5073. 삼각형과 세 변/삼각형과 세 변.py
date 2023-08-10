import sys
input = sys.stdin.readline

while True:
    data = list(map(int, input().rstrip().split()))
    if data == [0, 0, 0]:
        break
    else:
        data.sort()
        if data[2] >= data[0] + data[1]:
            print('Invalid')
        else:
            if data[0] == data[2]:
                print('Equilateral')
            elif (data[0] == data[1]) or (data[1] == data[2]):
                print('Isosceles')
            else:
                print('Scalene')