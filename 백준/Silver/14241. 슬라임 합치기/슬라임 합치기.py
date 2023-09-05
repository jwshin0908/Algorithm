import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
score = 0

while True:
    array.sort()
    score += array[-1] * array[-2]
    if len(array) == 2:
        print(score)
        break
    else:
        a = array.pop()
        b = array.pop()
        array.append(a + b)