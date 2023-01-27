data = []
for _ in range(9):
    data.append(int(input()))
a = max(data)
b = data.index(a)
print(a)
print(b+1)