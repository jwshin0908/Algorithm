import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())
C = int(input().rstrip())

if (A + B) >= C * 2:
    print((A + B) - C * 2)
else:
    print(A + B)