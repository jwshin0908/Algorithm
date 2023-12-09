import sys
input = sys.stdin.readline

N = int(input().rstrip())
D, P = 0, 0

for _ in range(N):
    win = input().rstrip()
    if win == 'D':
        D += 1
    else:
        P += 1
    if abs(D - P) == 2:
        print(f"{D}:{P}")
        break
else:
    print(f"{D}:{P}")