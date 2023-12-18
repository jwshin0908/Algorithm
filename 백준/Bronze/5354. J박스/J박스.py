import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n < 3:
        for _ in range(n):
            print('#' * n)
        print()
    else:
        print('#' * n)
        for _ in range(n - 2):
            print('#' + 'J' * (n - 2) + '#')
        print('#' * n, '\n')