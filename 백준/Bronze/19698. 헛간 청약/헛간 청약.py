import sys
input = sys.stdin.readline

N, W, H, L = map(int, input().rstrip().split())

print(min(N, (W // L) * (H // L)))