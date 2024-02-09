import sys
input = sys.stdin.readline

mbti = input().rstrip()
N = int(input().rstrip())
array = []

for _ in range(N):
    array.append(input().rstrip())
    
print(array.count(mbti))