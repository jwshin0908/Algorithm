import sys
input = sys.stdin.readline

n = int(input().rstrip())
distance = list(map(int, input().rstrip().split()))
price = list(map(int, input().rstrip().split()))
result = 0

# 첫 번째 도로는 항상 고정
c = price[0]
result = distance[0] * c

# 두 번째 도로부터 기존 도로보다 비용이 적을 경우 price update
for i in range(1, n - 1):
    if price[i] < c:
        c = price[i]
    result += distance[i] * c

print(result)