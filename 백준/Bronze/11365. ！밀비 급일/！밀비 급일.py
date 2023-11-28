import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == 'END':
        break
    else:
        print(sentence[::-1])