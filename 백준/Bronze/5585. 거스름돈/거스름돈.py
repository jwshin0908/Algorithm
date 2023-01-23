cost = int(input())
c = 1000-cost
data = [500,100,50,10,5,1]
result = []
for i in data:
    result.append(c//i)
    c = c%i
print(sum(result))