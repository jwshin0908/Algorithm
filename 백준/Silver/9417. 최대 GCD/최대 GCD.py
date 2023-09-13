import sys
input = sys.stdin.readline

N = int(input().rstrip())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for _ in range(N):
    array = list(map(int, input().rstrip().split()))
    gcd_list = []
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            gcd_list.append(gcd(array[i], array[j]))
    print(max(gcd_list))