N = int(input())
data = []
cnt = 0

for i in range(N):
    data.append(int(input()))
    
a = data[0] # 다솜이의 표
x = data[1:] # 나머지 후보들의 표
x.sort(reverse=True)

while True:
    x.sort(reverse=True)
    if len(x)==0:
        break
    if x[0]>=a:
        x[0]-=1
        a+=1
        cnt+=1
    else:
        break
print(cnt)
