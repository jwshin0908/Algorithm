# 각각 누적합을 구할 경우 시간 초과
# 각 자리까지의 누적합을 저장한 후에 j번째 누적합에서 i-1번째 누적합을 빼주는 방식
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

# 누적합 저장용 list
sum_array = [0]
sum = 0

for i in range(n):
    sum += nums[i]
    sum_array.append(sum)

for _ in range(m):
    i, j = map(int, input().rstrip().split())
    print(sum_array[j] - sum_array[i - 1])
