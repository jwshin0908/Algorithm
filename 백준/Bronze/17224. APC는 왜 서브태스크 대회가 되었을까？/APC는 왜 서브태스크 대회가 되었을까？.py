# 1차원 배열로 해결하기

N, L, K = map(int, input().split())
easy, hard = 0, 0
 
for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

# sub2까지 해결 가능한 문제 점수 먼저 더하기  
result = min(hard, K)*140

# sub2를 해결하고 남은 문제만큼 sub1 해결 점수 더하기
if hard < K:
    result+=min(K-hard, easy)*100

print(result)



# 부분 점수(list 정렬을 통한 문제 해결 시 2,3번 예제 해결 불가)

N, L, K = map(int, input().split())
result = 0
question = []
num = 0

for i in range(N):
    question.append(list(map(int, input().split())))
    
question.sort(key=lambda x: (x[1],x[0]))

for i in question:
    if i[1]<=L:
        result+=140
        num+=1
    elif i[0]<=L:
        result+=100
        num+=1
    if num==K:
        break

print(result)
