import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
array = sorted(list(map(int, input().rstrip().split())))
s = []

def backtracking(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    else:
        for i in range(start, N):
            s.append(array[i])
            backtracking(i)
            s.pop()

backtracking(0)