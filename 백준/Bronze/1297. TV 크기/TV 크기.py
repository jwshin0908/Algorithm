import sys
input = sys.stdin.readline

D, H, W = map(int, input().rstrip().split())

x = (D ** 2 / (H ** 2 + W ** 2)) ** 0.5

height = (H ** 2 * x ** 2) ** 0.5
width = (W ** 2 * x ** 2) ** 0.5

print(int(height), int(width))