from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
answer = []
stack = deque()
now = 1
flag = 0

for _ in range(n):
    num = int(input().rstrip())
    while now <= num:
        stack.append(now)
        answer.append('+')
        now += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        flag = 1
        print('NO')
        break
        
if flag == 0:
    for i in answer:
        print(i)