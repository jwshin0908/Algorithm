# Q01. 모험가 길드(p.311)

N = int(input()) # 모험가 수
data = list(map(int, input().split())) # 공포도 값 리스트

data.sort(reverse=True) # 내림차순으로 정렬

cnt = 0
for i in data: # 가장 큰 값 순으로 i에 들어감
  if N >= i: # 모험가 수가 i보다 크거나 같을 경우
    cnt+=1 # 집단 1개 형성
    N-=i # 모험가 수 i만큼 내림차순 리스트 앞에서부터 줄어듦(공포도 큰 값부터)
  else :
    break # 집단 형성 불가
    
print(cnt)