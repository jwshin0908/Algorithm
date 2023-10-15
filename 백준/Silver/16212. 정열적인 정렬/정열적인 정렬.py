import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = list(map(int, input().rstrip().split()))

array.sort()
print(' '.join(map(str, array)))