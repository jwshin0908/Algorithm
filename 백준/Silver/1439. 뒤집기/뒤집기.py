# 뒷자리랑 값이 다를 경우 cnt+1
# cnt 값의 짝,홀수 여부에 따라 다르게 출력

s = list(str(input()))
cnt = 0

for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        cnt+=1
if cnt%2==1:
    print(int((cnt+1)/2))
else:
    print(int(cnt/2))