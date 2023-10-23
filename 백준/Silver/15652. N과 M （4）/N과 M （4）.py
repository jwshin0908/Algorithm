import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
array = []

def backtracking(start):
    if len(array) == M:
        print(' '.join(map(str, array)))
        return
    else:
        for i in range(start, N + 1):
            array.append(i)
            backtracking(i)
            array.pop()

backtracking(1)