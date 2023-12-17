import sys
input = sys.stdin.readline

total = int(input().rstrip())
book_sum = 0

for _ in range(9):
    book_sum += int(input().rstrip())
    
print(total - book_sum)