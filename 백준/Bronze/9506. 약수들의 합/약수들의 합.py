import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == -1:
        break
    array = []
    for i in range(1, n):
        if n % i == 0:
            array.append(i)
    if n == sum(array):
        print(f"{n} = {' + '.join(map(str, array))}")
    else:
        print(f"{n} is NOT perfect.")