import sys
input = sys.stdin.readline

T = int(input().rstrip())

def distance(A, B):
    result = (A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2
    return result

for _ in range(T):
    data = []
    for _ in range(4):
        x, y = map(int, input().rstrip().split())
        data.append([x, y])
    data.sort()
    if (distance(data[0], data[1]) == distance(data[0], data[2]) == distance(data[1], data[3]) == distance(data[2], data[3])) and (distance(data[0], data[3]) == distance(data[1], data[2])):
        print(1)
    else:
        print(0)