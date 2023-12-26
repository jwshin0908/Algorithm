import sys
input = sys.stdin.readline

N = int(input().rstrip())
result = int(N ** 0.5)

print(f"The largest square has side length {result}.")