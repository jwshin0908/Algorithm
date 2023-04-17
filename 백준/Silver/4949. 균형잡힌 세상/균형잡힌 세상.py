import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break
    stack = []
    result = 'yes'
    left = '(['
    right = ')]'
    
    for i in s:
        # 왼쪽에 해당하면 스택에 넣어주기
        if i in left:
            stack.append(i)
        # 오른쪽에 해당할 때
        elif i in right:
            # 스택이 비어있었다면, 짝이 맞지 않음
            if len(stack) == 0:
                result = 'no'
                break
            # 비어있지 않아도, 짝이 안 맞을 경우
            elif right.index(i) != left.index(stack.pop()):
                result = 'no'
                break
    if len(stack) > 0:
        print('no')
    else:
        print(result)