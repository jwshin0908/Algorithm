data = list(map(int,input().split()))
data.sort()
if data[0]==data[-1]:
    print(10000+data[0]*1000)
elif data[0]==data[1] or data[1]==data[-1]:
    print(1000+data[1]*100)
else:
    print(data[-1]*100)