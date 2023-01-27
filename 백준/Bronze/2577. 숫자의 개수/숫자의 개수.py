data = []
for _ in range(3):
    data.append(int(input()))
multi = 1
for i in data:
    multi*=i

for j in range(10):
    print(str(multi).count(str(j)))