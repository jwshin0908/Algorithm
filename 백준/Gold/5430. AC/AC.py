from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    p = input().rstrip()
    n = int(input().rstrip())
    array = input().rstrip()[1:-1].split(',')
    queue = deque(array)
    R_cnt = 0
    
    if n == 0:
        queue = []
    for i in p:
        if i == 'R':
            R_cnt += 1
        elif i == 'D':
            if len(queue) == 0:
                print('error')
                break
            else:
                if R_cnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()                
    else:
        if R_cnt % 2 == 1:
            queue.reverse()
        print('[' + ','.join(queue) + ']')