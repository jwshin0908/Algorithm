import sys
input = sys.stdin.readline

x = int(input().rstrip())
y = int(input().rstrip())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)