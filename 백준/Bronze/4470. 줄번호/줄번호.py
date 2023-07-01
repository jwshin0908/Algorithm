import sys
input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n):
    x = input().rstrip()
    print(f"{i + 1}. {x}")