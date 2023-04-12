import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))
n.sort(reverse=True)

print(''.join(map(str, n)))