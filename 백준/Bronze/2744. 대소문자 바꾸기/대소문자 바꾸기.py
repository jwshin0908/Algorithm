import sys
input = sys.stdin.readline

S = input().rstrip()

for i in S:
    if i.isupper():
        i = i.lower()
    else:
        i = i.upper()
        
    print(i, end='')