import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = []
result = 0
for _ in range(N):
    array.append(int(input().rstrip()))
    
array.sort(reverse = True)

for i in range(N // 3):
    result += sum(array[3 * i:3 * i + 2])
    
if N % 3 != 0:
    result += sum(array[3 * (N // 3):])
    
print(result)