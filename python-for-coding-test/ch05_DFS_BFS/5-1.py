# 5-1. 스택 예제(p.126)

stack = []

# append() : 가장 뒤쪽에 원소 삽입
# pop() : 가장 뒤쪽에서 데이터 꺼냄
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# 최하단부터 출력
print(stack)

# 최상단부터 출력(먼저 나가게 될 원소부터)
print(stack[::-1])