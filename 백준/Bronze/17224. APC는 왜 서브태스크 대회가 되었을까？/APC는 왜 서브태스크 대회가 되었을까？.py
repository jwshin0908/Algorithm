N, L, K = map(int, input().split())
result = 0
question = []
num = K

for i in range(N):
    question.append(list(map(int, input().split())))
    
question.sort(key=lambda x: (x[1],x[0]))

for i in question:
    if i[1]<=L:
        result+=140
        num-=1
    elif i[0]<=L:
        result+=100
        num-=1
    if num==0:
        break

print(result)