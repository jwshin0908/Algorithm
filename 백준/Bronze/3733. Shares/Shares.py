import sys
input = sys.stdin.readline

result = []
while True:
    try:
        a, b = map(int, input().rstrip().split())
        result.append(b // (a + 1))
    except:
        for i in result:
            print(i)
        break