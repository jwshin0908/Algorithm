import sys
input = sys.stdin.readline

a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

print(max(sum(a), sum(b)))