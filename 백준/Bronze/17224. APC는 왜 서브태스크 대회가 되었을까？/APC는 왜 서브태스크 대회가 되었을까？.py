# 난이도를 sub2 다음 sub1 순으로 정렬

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