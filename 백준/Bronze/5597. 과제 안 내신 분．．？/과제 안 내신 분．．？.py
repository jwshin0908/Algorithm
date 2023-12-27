import sys
input = sys.stdin.readline

array = []
for _ in range(28):
    array.append(int(input().rstrip()))
    
for i in range(1, 31):
    if i not in array:
        print(i)