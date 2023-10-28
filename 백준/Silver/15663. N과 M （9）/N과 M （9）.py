import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
array = sorted(list(map(int, input().rstrip().split())))
s = []
visited = [False] * N

def backtracking():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    else:
        pre = 0
        for i in range(N):
            if (not visited[i]) and (pre != array[i]):
                visited[i] = True
                s.append(array[i])
                pre = array[i]
                backtracking()
                visited[i] = False
                s.pop()
                
backtracking()