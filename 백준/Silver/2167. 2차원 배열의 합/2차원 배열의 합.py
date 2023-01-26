# array를 통해 누적합 sum_array 생성

n, m = map(int, input().split())
array = []
sum_array = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(n):
    array.append(list(map(int, input().split())))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_array[i][j] = array[i - 1][j - 1] + sum_array[i - 1][j] + sum_array[i][j - 1] - sum_array[i - 1][j - 1]

# sum_array를 이용해 누적합 계산(https://hynnjnn.tistory.com/17 참고)
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(sum_array[x][y] - sum_array[x][j - 1] - sum_array[i - 1][y] + sum_array[i - 1][j - 1])
    
    
    
# 시간 초과 코드
N, M = map(int, input().split())
array = []
for _ in range(N):
  array.append(list(map(int, input().split())))
K = int(input())
sum_array = []

for _ in range(K):
  sum_array.append(list(map(int, input().split())))

# [i,j,x,y]을 통해 행 index가 range(i-1, x), 열 index가 range(j-1, y) 이내 array 누적 합
for i in range(K):
  sum = 0
  for j in range(sum_array[i][0] - 1, sum_array[i][2]):
    for k in range(sum_array[i][1] - 1, sum_array[i][3]):
      sum += array[j][k]
  print(sum)
