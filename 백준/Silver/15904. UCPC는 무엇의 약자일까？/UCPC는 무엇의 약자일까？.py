import sys
input = sys.stdin.readline

word = input().rstrip().replace(' ','')
answer = 'UCPC'
idx = 0

for i in word:
    if i == answer[idx]:
        idx += 1
    if idx == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')