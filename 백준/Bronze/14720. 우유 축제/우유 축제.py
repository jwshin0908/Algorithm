n = int(input())
data = list(map(int, input().split()))
cnt = 0

for i in range(n):
    # 우유 가게에서 파는 우유 종류 = 이번에 마실 우유 종류 -> cnt 1 증가
    if data[i]==cnt%3:
        cnt+=1
        
print(cnt)
