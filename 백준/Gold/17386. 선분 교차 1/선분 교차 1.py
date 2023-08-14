import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().rstrip().split())
x3, y3, x4, y4 = map(int, input().rstrip().split())

A = (x1, y1)
B = (x2, y2)
C = (x3, y3)
D = (x4, y4)

def CCW(X, Y, Z):
    result = (X[0] * Y[1] + Y[0] * Z[1] + Z[0] * X[1]) - (X[1] * Y[0] + Y[1] * Z[0] + Z[1] * X[0])
    if result > 0: # 반시계
        return 1
    elif result < 0: # 시계
        return -1
    else:
        return 0

if (CCW(A, B, C) * CCW(A, B, D) == -1) and (CCW(C, D, A) * CCW(C, D, B) == -1):
    print(1)
else:
    print(0)