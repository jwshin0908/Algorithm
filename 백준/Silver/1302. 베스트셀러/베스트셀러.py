import sys
input = sys.stdin.readline

n = int(input().rstrip())
book = {}

for _ in range(n):
    x = input().rstrip()
    if x in book.keys():
        book[x] += 1
    else:
        book[x] = 1

result = [k for k, v in book.items() if max(book.values()) == v]
result.sort()

print(result[0])