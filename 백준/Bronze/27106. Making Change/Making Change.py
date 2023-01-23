n = int(input())
c = 100-n
result = []
data = [25, 10, 5, 1]

for i in data:
    result.append(c//i)
    c = c%i

print(" ".join(map(str,result)))