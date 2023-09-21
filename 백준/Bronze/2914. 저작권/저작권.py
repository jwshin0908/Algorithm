import sys
input = sys.stdin.readline

cnt, mean = map(int, input().rstrip().split())
result = (mean - 1) * cnt + 1

print(result)