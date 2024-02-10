import sys
input = sys.stdin.readline

R = int(input().rstrip())
C = int(input().rstrip())

for _ in range(R):
    print('*' * C)