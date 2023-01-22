T = int(input())
data = []
for i in range(T):
    data.append(int(input()))
money = [25, 10, 5, 1]
result = []
for j in data:
    l = []
    for k in money:
        l.append(j // k)
        j = j % k
    result.append(l)
for r in result:
    print(' '.join(map(str,r)))