import sys
input = sys.stdin.readline

burger = []
drink = []

for _ in range(3):
    burger.append(int(input().rstrip()))

for _ in range(2):
    drink.append(int(input().rstrip()))

print(min(burger) + min(drink) - 50)