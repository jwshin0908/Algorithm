import sys
input = sys.stdin.readline

array = []
for _ in range(5):
    array.append(int(input().rstrip()))
    
for i in set(array):
    if array.count(i) % 2 == 1:
        print(i)