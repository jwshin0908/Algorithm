# 스택 자료 구조
import sys
input = sys.stdin.readline

k = int(input().rstrip())
stack = []

for _ in range(k):
    x = int(input().rstrip())
    if x != 0:
        stack.append(x)
    else:
        stack.pop()

result = sum(stack)
print(result)