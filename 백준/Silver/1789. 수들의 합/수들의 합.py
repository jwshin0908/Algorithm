s = int(input())
n = 0
while True:
    n += 1
    if n * (n + 1) / 2 >= s - n:
        break
print(n)