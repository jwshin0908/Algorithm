import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

a, b = 100 - A, 100 - B
c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100

print(a, b, c, d, q, r)
print(c + q, r)