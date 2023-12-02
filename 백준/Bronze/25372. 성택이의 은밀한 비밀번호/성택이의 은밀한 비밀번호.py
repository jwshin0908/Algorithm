import sys
input = sys.stdin.readline

N = int(input().rstrip())

for _ in range(N):
    code = input().rstrip()
    if len(code) >= 6 and len(code) <=9:
        print('yes')
    else:
        print('no')