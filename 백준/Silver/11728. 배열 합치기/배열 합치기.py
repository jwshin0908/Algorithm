import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))

result = A + B
result.sort()

print(' '.join(map(str, result)))