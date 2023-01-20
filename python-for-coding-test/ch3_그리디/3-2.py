# 3-2. 큰 수의 법칙(p.92)

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)            

sum = M//(K+1) * (data[0]*K + data[1]) + M%(K+1) * data[0]
print(sum)