import sys
input = sys.stdin.readline

for _ in range(2):
    T, F, S, P, C = map(int, input().rstrip().split())
    score = 6 * T + 3 * F + 2 * S + 1 * P + 2 * C
    print(score)