import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().rstrip().split())
result = [w - x, x, h - y, y]

print(min(result))