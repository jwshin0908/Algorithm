import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
word_set = set()
cnt = 0

for _ in range(N):
    word = input().rstrip()
    word_set.add(word)

for _ in range(M):
    test = input().rstrip()
    if test in word_set:
        cnt += 1

print(cnt)