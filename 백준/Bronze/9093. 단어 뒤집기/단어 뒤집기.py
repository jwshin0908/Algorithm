import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    sentence = list(input().rstrip().split())
    for i in sentence:
        print(i[::-1], end=' ')
    print()
