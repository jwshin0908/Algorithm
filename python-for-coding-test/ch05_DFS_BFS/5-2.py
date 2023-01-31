# 5-2. 큐 예제(p.129)

from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# append() : list의 append와 동일(가장 오른쪽에 데이터 추가)
# popleft() : 가장 왼쪽의 데이터 꺼내기
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# 들어온 순서대로 출력
print(queue)
print(list(queue))

# 나중에 들어온 원소 순서대로 출력
queue.reverse()
print(queue)
print(list(queue))