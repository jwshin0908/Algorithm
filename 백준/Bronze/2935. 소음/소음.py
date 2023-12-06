import sys
input = sys.stdin.readline

A = int(input().rstrip())
c = input().rstrip()
B = int(input().rstrip())

if c == '*':
    print(A * B)
elif c == '+':
    print(A + B)