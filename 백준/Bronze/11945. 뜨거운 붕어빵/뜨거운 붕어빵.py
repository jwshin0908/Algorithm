import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
for _ in range(N):
    fish = input().rstrip()
    print(fish[::-1])