import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
array = sorted(list(map(int, input().rstrip().split())))
s = []

def backtracking():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    else:
        for i in array:
            if i not in s:
                s.append(i)
                backtracking()
                s.pop()
backtracking()      