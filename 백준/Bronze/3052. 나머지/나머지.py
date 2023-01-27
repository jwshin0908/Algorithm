data = []
for _ in range(10):
    data.append(int(input()))
result = []
for i in data:
    result.append(i%42)
result = set(result)
print(len(result))