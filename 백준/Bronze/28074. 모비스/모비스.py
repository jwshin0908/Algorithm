import sys
input = sys.stdin.readline

word = input().rstrip()
array = ['M', 'O', 'B', 'I', 'S']

result = 'YES'
for i in array:
    if i not in word:
        result = 'NO'
        break
print(result)