import sys
input = sys.stdin.readline

sentence = input().rstrip()
word = input().rstrip()
length = len(word)
cnt = 0

while True:
    index = sentence.find(word)
    if index != -1:
        cnt += 1
        if index + length >= len(sentence):
            break
        else:
            sentence = sentence[index + length:]
    else:
        break

print(cnt)