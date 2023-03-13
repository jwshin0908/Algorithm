import sys

input = sys.stdin.readline

n = int(input().rstrip())
array = []

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    array.append([a, b])

# key에 대해 기준이 2개 이상일 경우 ()로 묶어주기
result = sorted(array, key=lambda x: (x[1], x[0]))

for i in result:
    print(' '.join(map(str, i)))
