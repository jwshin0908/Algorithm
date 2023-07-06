import sys
input = sys.stdin.readline

word = input().rstrip()
n = int(input().rstrip())
array = [input().rstrip() for _ in range(n)]
cnt = 0

for i in array:
    if word in i * 2:
        cnt += 1

print(cnt)