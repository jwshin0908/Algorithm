s = list(input())
ascii = [ord(i) for i in s]
for j in range(97, 123):
    if j in ascii:
        print(ascii.index(j), end=' ')
    else:
        print(-1, end=' ')
        
# 간단한 코드
s = input()
for i in range(97,123):
    print(s.find(chr(i)), end=' ')
