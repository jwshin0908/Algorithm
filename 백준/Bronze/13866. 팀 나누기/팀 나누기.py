import sys
input = sys.stdin.readline

A, B, C, D = map(int, input().rstrip().split())

print(abs((A + D) - (B + C)))