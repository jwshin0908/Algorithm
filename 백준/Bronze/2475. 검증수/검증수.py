data = list(map(int, input().split()))
sum = 0
for i in data:
    sum+=i*i
print(sum%10)