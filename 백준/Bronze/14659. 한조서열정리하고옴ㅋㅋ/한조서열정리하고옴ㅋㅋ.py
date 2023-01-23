# N=10^5, 이중 for문 : O(N^2)=10^10(시간 초과)
# 단일 for문 : O(N) -> data에서 한 칸씩 옮기고, if 불만족시 비교 값 변경
# 내림차순일 경우 또한 고려해야 함.

n = int(input())
data = list(map(int, input().split()))
x = data[0]
cnt = 0
result = []

for i in range(1,n):
    if data[i]<x:
        cnt+=1
    else:
        x = data[i]
        result.append(cnt)
        cnt=0

# 내림차순으로 정렬되어 0번이 나머지를 모두 처리 가능할 때
result.append(cnt)
print(max(result))