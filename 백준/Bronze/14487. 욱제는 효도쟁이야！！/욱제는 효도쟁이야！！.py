n = int(input())
data = list(map(int, input().split()))
data.sort()

print(sum(data)-data[-1])