import sys
input = sys.stdin.readline

quiz = input().rstrip()
a = int(quiz[0])
b = int(quiz[4])
c = int(quiz[-1])

if a + b == c:
    print('YES')
else:
    print('NO')