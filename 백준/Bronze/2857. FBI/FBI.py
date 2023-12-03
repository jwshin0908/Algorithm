import sys
input = sys.stdin.readline

array = []
for i in range(5):
    agent = input().rstrip()
    if 'FBI' in agent:
        array.append(i + 1)

if len(array) > 0:
    print(' '.join(map(str, array)))
else:
    print('HE GOT AWAY!')