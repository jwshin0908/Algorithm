N, K = map(int, input().split())
data = []
cnt = 0
for _ in range(N):
    data.append(int(input()))

data.sort(reverse=True)

for i in data:
    cnt+=K//i
    K%=i

print(cnt)