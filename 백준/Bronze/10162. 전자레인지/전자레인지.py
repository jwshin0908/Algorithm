# A - 300s, B - 60s, C - 10s
t = int(input())

data = [300, 60, 10]
result = []
for i in data:
    result.append(t//i)
    t = t%i

if t!=0:
    print(-1)
else:
    print(' '.join(map(str, result)))