N = int(input())
data = list(map(int, input().split()))

M = max(data)
new_data = [i/M*100 for i in data]
print(sum(new_data)/N)