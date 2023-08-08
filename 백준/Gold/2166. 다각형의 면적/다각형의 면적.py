import sys
input = sys.stdin.readline

N = int(input().rstrip())
total = []
for _ in range(N):
    total.append(list(map(int, input().rstrip().split())))

total.append(total[0])
result = 0

for i in range(N):
    result += total[i][0] * total[i + 1][1]
    result -= total[i][1] * total[i + 1][0]

print(round(1 / 2 * abs(result), 1))