import sys
input = sys.stdin.readline

array = []
for _ in range(3):
    array.append(int(input().rstrip()))
    
array.sort()
print(array[1])