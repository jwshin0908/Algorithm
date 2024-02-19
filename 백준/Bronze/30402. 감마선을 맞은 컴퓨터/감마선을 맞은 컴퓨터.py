import sys
input = sys.stdin.readline

for _ in range(15):
    word = input().rstrip().split()
    if 'w' in word:
        print('chunbae')
        break
    elif 'b' in word:
        print('nabi')
        break
    elif 'g' in word:
        print('yeongcheol')
        break
    else:
        continue