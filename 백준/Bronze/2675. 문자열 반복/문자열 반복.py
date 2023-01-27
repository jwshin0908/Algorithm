t = int(input())
for i in range(t):
    x, y = input().split()
    for j in y:
        print(int(x)*j, end='')
    print()
