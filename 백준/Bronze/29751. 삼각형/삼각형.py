import sys
input = sys.stdin.readline

W, H = map(int, input().rstrip().split())

print(W * H * 0.5)