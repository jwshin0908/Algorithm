import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
result = a * (100 - b) * 0.01

if result < 100:
    print(1)
else:
    print(0)