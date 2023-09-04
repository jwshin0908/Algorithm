import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = list(map(int, input().rstrip().split()))

array.sort(reverse = True)

result = array[0] + sum(array[1:]) / 2

print(result)