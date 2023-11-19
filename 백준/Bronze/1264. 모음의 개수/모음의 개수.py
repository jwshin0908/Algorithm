import sys
input = sys.stdin.readline

target = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    word = input().rstrip()
    if word == '#':
        break
    cnt = 0
    for i in word:
        if i in target:
            cnt += 1
    print(cnt)