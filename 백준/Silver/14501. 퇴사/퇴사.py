import sys
input = sys.stdin.readline

N = int(input().rstrip())
work = []
d = [0] * (N + 1)

for _ in range(N):
    work.append(list(map(int, input().rstrip().split())))
    
for i in range(N - 1, -1, -1):
    if i + work[i][0] > N:
        d[i] = d[i + 1]
    else:
        d[i] = max(d[i + 1], d[i + work[i][0]] + work[i][1])
        
print(d[0])