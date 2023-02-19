sum = 0
for _ in range(4):
    sum += int(input())
    
x = sum//60
y = sum%60

print(x)
print(y)