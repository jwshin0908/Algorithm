import sys
input = sys.stdin.readline

K, D, A = map(int, input().rstrip().split('/'))

if (K + A < D) or D == 0:
    print('hasu')
else:
    print('gosu')