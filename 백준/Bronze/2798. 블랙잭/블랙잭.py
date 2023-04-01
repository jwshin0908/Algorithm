from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
cards = list(map(int, input().rstrip().split()))

x = combinations(cards, 3)
y = []

for i in x:
    y.append(sum(i))

z = [i for i in y if i <= m]
z.sort()

print(z[-1])