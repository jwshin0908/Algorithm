import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))

first = array[0]
rest = array[1:]

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for i in rest:
    G = int(gcd(first, i))
    new_first = int(first // G)
    new_i = int(i // G)
    print(f"{new_first}/{new_i}")