import sys
input = sys.stdin.readline

x = int(input().rstrip())

if (620 <= x) and (x <= 780):
    print('Red')
elif (590 <= x) and (x < 620):
    print('Orange')
elif (570 <= x) and (x < 590):
    print('Yellow')
elif (495 <= x) and (x < 570):
    print('Green')
elif (450 <= x) and (x < 495):
    print('Blue')
elif (425 <= x) and (x < 450):
    print('Indigo')
elif (380 <= x) and (x < 425):
    print('Violet')