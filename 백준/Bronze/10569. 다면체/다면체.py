import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    V, E = map(int, input().rstrip().split())
    result = 2 - V + E
    print(result)