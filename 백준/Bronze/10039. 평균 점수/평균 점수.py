array = []
for _ in range(5):
    array.append(int(input()))

sum = 0
for i in array:
    if i<40:
        sum+=40
    else:
        sum+=i
print(int(sum//5))