import sys
input = sys.stdin.readline

score = 0
for _ in range(5):
    score += int(input().rstrip())
    
print(score)