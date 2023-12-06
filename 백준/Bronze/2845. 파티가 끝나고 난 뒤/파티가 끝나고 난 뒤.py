import sys
input = sys.stdin.readline

L, P = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))
cnt = L * P

for i in array:
    print(i - cnt, end = ' ')