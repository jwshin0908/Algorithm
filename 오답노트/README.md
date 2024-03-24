[1. 시뮬레이션](#1-시뮬레이션)<br/>
&emsp;[(1) dx dy technique](#1-dx-dy-technique)<br/>
&emsp;[(2) 객체](#2-객체)<br/>
&emsp;[(3) 일반 정렬](#3-일반-정렬)<br/>
&emsp;[(4) 객체 정렬](#4-객체-정렬)<br/>
&emsp;[(5) 격자 안에서 완전 탐색](#5-격자-안에서-완전-탐색)<br/>
&emsp;[(6) 격자 안에서 밀고 당기기](#6-격자-안에서-밀고-당기기)<br/>
&emsp;[(7) 격자 안에서 터지고 떨어지는 경우](#7-격자-안에서-터지고-떨어지는-경우)<br/>
&emsp;[(8) 격자 안에서 단일 객체를 이동](#8-격자-안에서-단일-객체를-이동)<br/>
&emsp;[(9) 격자 안에서 여러 객제를 이동](#9-격자-안에서-여러-객제를-이동)<br/>

[2. 백트래킹](#2-백트래킹)<br/>


# 1. 시뮬레이션
## (1) dx dy technique

<details>
<summary>코드 토글</summary>
<div markdown="1">

```Python3
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
```
</div>
</details>


## (2) 객체

## (3) 일반 정렬

## (4) 객체 정렬

## (5) 격자 안에서 완전 탐색
<details>
<summary>코드 토글</summary>
<div markdown="1">

```Python3
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

def same_number(arr, n, m):
    max_cnt = 1
    cnt = 1
    num = arr[0]
    for i in range(1, n):
        if arr[i] == num:
            cnt += 1
        else:
            cnt = 1
        num = arr[i]
        max_cnt = max(max_cnt, cnt)
    if max_cnt >= m:
        return 1
    else:
        return 0

result = 0

for i in range(n):
    arr = []
    for j in range(n):
        arr.append(array[i][j])
    result += same_number(arr, n, m)


for j in range(n):
    arr = []
    for i in range(n):
        arr.append(array[i][j])
    result += same_number(arr, n, m)

print(result)
```
</div>
</details>



## (6) 격자 안에서 밀고 당기기

## (7) 격자 안에서 터지고 떨어지는 경우

## (8) 격자 안에서 단일 객체를 이동

## (9) 격자 안에서 여러 객제를 이동
<details>
<summary>코드 토글</summary>
<div markdown="1">

```Python3

```
</div>
</details>


# 2. 백트래킹
