import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = []

def round_num(x):
    return int(x) + (1 if (x - int(x)) >= 0.5 else 0)

if n == 0:
    print(0)
else:
    for _ in range(n):
        array.append(int(input().rstrip()))

    array.sort()

    cut = round_num(n * 0.15)
    new_array = array[cut:n - cut]
    
    if len(new_array) == 0:
        print(0)
    else:
        result = sum(new_array) / len(new_array)
        print(round_num(result))