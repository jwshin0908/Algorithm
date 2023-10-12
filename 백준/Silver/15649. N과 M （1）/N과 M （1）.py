import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
s = []

def backtracking():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        if i not in s:
            s.append(i)
            backtracking()
            s.pop()
            
backtracking()