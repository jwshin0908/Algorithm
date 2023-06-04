import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

pokemon_name = dict()
pokemon_num = dict()

for i in range(1, n + 1):
    x = input().rstrip()
    pokemon_name[x] = i
    pokemon_num[i] = x

for _ in range(m):
    y = input().rstrip()
    if y.isdigit():
        # int를 해줘야 함
        print(pokemon_num[int(y)])
    else:
        print(pokemon_name[y])