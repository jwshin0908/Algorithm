import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    s = sys.stdin.readline().rstrip()
    while '()' in s:
        try:
            s = s.replace('()', '')
        except:
            break
    if s == '':
        print('YES')
    else:
        print('NO')