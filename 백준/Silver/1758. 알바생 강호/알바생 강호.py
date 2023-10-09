import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = []

for _ in range(N):
    array.append(int(input().rstrip()))
    
array.sort(reverse = True)
minus = [i for i in range(N)]

result = 0
for i in range(N):
    pay = array[i] - minus[i]
    if pay >= 0:
        result += pay
        
print(result)