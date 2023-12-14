import sys
input = sys.stdin.readline

N = int(input().rstrip())
cnt_A, cnt_B = 0, 0

for _ in range(N):
    A, B = map(int, input().rstrip().split())
    if A > B:
        cnt_A += 1
    elif A < B:
        cnt_B += 1
        
print(cnt_A, cnt_B)