# while에 else문 사용
# 방식 : 5로 나눠지면 몫 사용, 아니면 3씩 빼면서 5로 나누기 시도
N = int(input())
cnt = 0

while N>=0:
    if N%5==0:
        cnt+=N//5
        print(cnt)
        break
    else:
        N-=3
        cnt+=1
else:
    print(-1)