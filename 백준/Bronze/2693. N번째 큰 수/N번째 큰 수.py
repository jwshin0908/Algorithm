import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    array = list(map(int, input().rstrip().split()))
    array.sort(reverse = True)
    print(array[2])