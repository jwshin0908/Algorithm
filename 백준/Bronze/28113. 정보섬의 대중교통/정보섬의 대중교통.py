import sys
input = sys.stdin.readline

N, A, B = map(int, input().rstrip().split())

if A > max(N, B):
    print('Subway')
elif A < max(N, B):
    print('Bus')
else:
    print('Anything')