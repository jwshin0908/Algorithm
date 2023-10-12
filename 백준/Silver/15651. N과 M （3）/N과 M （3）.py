import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
s = []

def backtracking():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    else:
        for i in range(1, N + 1):
            s.append(i)
            backtracking()
            s.pop()
            
backtracking()            