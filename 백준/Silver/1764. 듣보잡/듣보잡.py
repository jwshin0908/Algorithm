import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
hear = list()
see = list()

for _ in range(n):
    hear.append(input().rstrip())

for _ in range(m):
    see.append(input().rstrip())

result = list(set(hear).intersection(set(see)))
result.sort()

print(len(result))
for i in result:
    print(i)
