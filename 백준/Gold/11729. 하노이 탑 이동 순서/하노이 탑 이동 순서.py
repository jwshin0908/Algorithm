import sys
input = sys.stdin.readline

N = int(input().rstrip())

def func(n, start, end):
    if n == 1:
        print(start, end)
        return
    else:
        func(n - 1, start, 6 - start - end)
        print(start, end)
        func(n - 1, 6 - start - end, end)
        
print(2 ** N - 1)
func(N, 1, 3)