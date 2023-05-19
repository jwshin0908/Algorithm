import sys
input = sys.stdin.readline

word = input().rstrip()
array = []
length = len(word)

for i in range(length - 2):
    for j in range(i + 1, length - 1):
        x, y, z = word[:i + 1], word[i + 1:j + 1], word[j + 1:]
        x = x[::-1]
        y = y[::-1]
        z = z[::-1]
        array.append(x + y + z)

array.sort()

print(array[0])