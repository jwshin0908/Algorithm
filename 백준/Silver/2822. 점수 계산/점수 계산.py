import sys
input = sys.stdin.readline

array = []
for _ in range(8):
    array.append(int(input().rstrip()))

result = sorted(array, reverse=True)[:5]
score = sum(result)
q = []
for i in result:
    q.append(1 + array.index(i))
q.sort()

print(score)
print(' '.join(map(str, q)))