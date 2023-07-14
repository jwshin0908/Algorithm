import sys
input = sys.stdin.readline

x = int(input().rstrip())
n = int(input().rstrip())
price = 0

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    price += a * b

if price == x:
    print('Yes')
else:
    print('No')