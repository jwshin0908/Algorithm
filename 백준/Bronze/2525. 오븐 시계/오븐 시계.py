a, b = map(int, input().split())
c = int(input())

h = int(c//60)
m = int(c%60)

if b+m>=60:
    a+=1
    b_new = b+m-60
else:
    b_new = b+m

if a+h>=24:
    a_new = a+h-24
else:
    a_new = a+h
    
print(a_new, b_new)