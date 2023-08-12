import sys
input = sys.stdin.readline

x1, y1, x2, y2, x3, y3 = map(int, input().rstrip().split())

A = (x1, y1)
B = (x2, y2)
C = (x3, y3)

def distance(X, Y):
    result = ((X[0]- Y[0]) ** 2 + (X[1] - Y[1]) ** 2) ** 0.5
    return result

dis = [distance(A, B), distance(B, C), distance(C, A)]
dis.sort()

tri_area = (A[0] * B[1] + B[0] * C[1] + C[0] * A[1]) - (A[1] * B[0] + B[1] * C[0] + C[1] * A[0])
if tri_area == 0:
    print(-1)
else:
    print((dis[2] - dis[0]) * 2)