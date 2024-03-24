코드트리

[1. 시뮬레이션](#1-시뮬레이션)<br/>
&emsp;[(1) dx dy technique](#1-dx-dy-technique)<br/>
&emsp;[(2) 객체](#2-객체)<br/>
&emsp;[(3) 일반 정렬](#3-일반-정렬)<br/>
&emsp;[(4) 객체 정렬](#4-객체-정렬)<br/>
&emsp;[(5) 격자 안에서 완전 탐색](#5-격자-안에서-완전-탐색)<br/>



# 1. 시뮬레이션
## (1) dx dy technique

````
N = int(input())
array = []
for _ in range(N):
    array.append(list(input()))
loc = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir_num = (loc - 1) // N

if loc <= N:
    x = 0
    y = loc - 1
elif loc <= 2 * N:
    x = loc - N - 1
    y = N - 1
elif loc <= 3 * N:
    x = N - 1
    y = N - (loc - 2 * N)
elif loc <= 4 * N:
    x = N - (loc - 3 * N)
    y = 0

def in_range(x, y):
    return (0 <= x and x < N) and (0 <= y and y < N)

cnt = 1

while True:
    mirror = array[x][y]
    if mirror == '/':
        if (dir_num % 2 == 1):
            dir_num = (dir_num + 3) % 4
        else:
            dir_num = (dir_num + 1) % 4
    else:
        if (dir_num % 2 == 1):
            dir_num = (dir_num + 1) % 4
        else:
            dir_num = (dir_num + 3) % 4
    x = x + dx[dir_num]
    y = y + dy[dir_num]
    if in_range(x, y) == False:
        break
    cnt += 1
    
print(cnt)
````
## (2) 객체

## (3) 일반 정렬

## (4) 객체 정렬

## (5) 격자 안에서 완전 탐색
