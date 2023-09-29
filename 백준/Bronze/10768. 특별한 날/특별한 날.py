import sys
input = sys.stdin.readline

month = int(input().rstrip())
day = int(input().rstrip())

if month == 1:
    print('Before')
elif month >= 3:
    print('After')
else:
    if day < 18:
        print('Before')
    elif day > 18:
        print('After')
    else:
        print('Special')