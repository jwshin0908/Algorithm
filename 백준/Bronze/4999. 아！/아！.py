import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

if B in A:
    print('go')
else:
    print('no')