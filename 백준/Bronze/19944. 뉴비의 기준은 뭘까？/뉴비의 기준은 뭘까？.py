import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

if M <= 2:
    print('NEWBIE!')
elif M <= N:
    print('OLDBIE!')
else:
    print('TLE!')