n = int(input())
data = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if data[i]==cnt%3:
        cnt+=1
        
print(cnt)