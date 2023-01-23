# input이 계속 들어올 수 있음에 유의

while True:
    try:
        a, b, c = map(int, input().split())
        print(max(b-a, c-b)-1)
    except:
        break