import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
set_a = set(map(int, input().rstrip().split()))
set_b = set(map(int, input().rstrip().split()))
result = len(set_a - set_b) + len(set_b - set_a)

print(result)