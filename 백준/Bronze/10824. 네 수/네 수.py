import sys
input = sys.stdin.readline

A, B, C, D = input().rstrip().split()

first = int(A + B)
second = int(C + D)

print(first + second)