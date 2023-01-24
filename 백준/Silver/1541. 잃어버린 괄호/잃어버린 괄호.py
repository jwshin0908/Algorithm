# '-' 기준으로 split, 이후 '+' 기준으로 split해서 int로 바꿔 계산
# <error> 'int' object is not callable : 예약어를 변수명으로 사용시 발생
# sum(list) 대신 list for문을 통해 하나씩 계산하기

s = str(input())
data_minus = s.split('-')
result = []

for i in data_minus:
    sum = 0
    data_plus = i.split('+')
    for j in data_plus:
        sum+=int(j)
    result.append(sum)

x = result[0]
for j in range(1,len(result)):
    x-=result[j]
    
print(x)